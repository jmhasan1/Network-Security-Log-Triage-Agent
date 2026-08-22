import hashlib
import subprocess
import sys
from pathlib import Path

import tomllib
import json
import tempfile


PROJECT_ROOT = Path(__file__).resolve().parents[4]
PYPROJECT_PATH = PROJECT_ROOT / "pyproject.toml"
UV_LOCK_PATH = PROJECT_ROOT / "uv.lock"
DATASET_DVC_PATH = PROJECT_ROOT / "data" / "raw" / "phisingData.csv.dvc"
DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "phisingData.csv"


def _run_git_command(*args: str) -> str:
    """Run a Git command and return its output."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def _get_project_metadata() -> dict:
    """Read project metadata from pyproject.toml."""
    try:
        with open(PYPROJECT_PATH, "rb") as file:
            pyproject = tomllib.load(file)

        project = pyproject.get("project", {})

        return {
            "project_name": project.get("name", "unknown"),
            "project_version": project.get("version", "unknown"),
        }

    except (FileNotFoundError, tomllib.TOMLDecodeError):
        return {
            "project_name": "unknown",
            "project_version": "unknown",
        }


def _get_git_metadata() -> dict:
    """Collect Git repository metadata."""
    return {
        "git_commit": _run_git_command("rev-parse", "HEAD"),
        "git_branch": _run_git_command(
            "rev-parse", "--abbrev-ref", "HEAD"
        ),
    }


def _get_dataset_metadata() -> dict:
    """Collect metadata for the DVC-tracked dataset."""
    metadata = {
        "dataset_version": "dataset-v001",
        "dataset_dvc_hash": "unknown",
        "dataset_sha256": "unknown",
    }

    try:
        if DATASET_DVC_PATH.exists():
            dvc_text = DATASET_DVC_PATH.read_text(encoding="utf-8")

            for line in dvc_text.splitlines():
                if "md5:" in line:
                    metadata["dataset_dvc_hash"] = (
                        line.split("md5:", 1)[1].strip()
                    )
                    break

        if DATASET_PATH.exists():
            sha256 = hashlib.sha256()

            with open(DATASET_PATH, "rb") as file:
                for chunk in iter(lambda: file.read(1024 * 1024), b""):
                    sha256.update(chunk)

            metadata["dataset_sha256"] = sha256.hexdigest()

    except OSError:
        pass

    return metadata


def _get_environment_metadata() -> dict:
    """Collect runtime/environment metadata."""
    return {
        "python_version": sys.version.split()[0],
        "environment_manager": "uv",
        "lockfile_hash": _get_file_sha256(UV_LOCK_PATH),
    }


def collect_lineage() -> dict:
    """
    Collect project, Git, dataset, and environment lineage metadata.
    """
    project = _get_project_metadata()
    git = _get_git_metadata()
    dataset = _get_dataset_metadata()
    environment = _get_environment_metadata()

    return {
        **project,
        **git,
        **dataset,
        "feature_version": "v1",
        "preprocessing_version": "v1",
        **environment,
    }

def _get_file_sha256(file_path: Path) -> str:
    """Calculate SHA-256 for a file."""
    if not file_path.exists():
        return "unknown"

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()

def create_lineage_artifacts(lineage: dict) -> dict:
    """
    Create temporary lineage artifact files for MLflow.

    Returns
    -------
    dict
        Mapping of artifact type to temporary file path.
    """
    temp_dir = Path(tempfile.mkdtemp(prefix="network_security_lineage_"))

    provenance_dir = temp_dir / "provenance"
    dataset_dir = temp_dir / "dataset"
    environment_dir = temp_dir / "environment"

    provenance_dir.mkdir(parents=True, exist_ok=True)
    dataset_dir.mkdir(parents=True, exist_ok=True)
    environment_dir.mkdir(parents=True, exist_ok=True)

    git_info = {
        "git_commit": lineage["git_commit"],
        "git_branch": lineage["git_branch"],
        "project_name": lineage["project_name"],
        "project_version": lineage["project_version"],
    }

    dataset_metadata = {
        "dataset_version": lineage["dataset_version"],
        "dataset_dvc_hash": lineage["dataset_dvc_hash"],
        "dataset_sha256": lineage["dataset_sha256"],
        "feature_version": lineage["feature_version"],
        "preprocessing_version": lineage["preprocessing_version"],
    }

    git_info_path = provenance_dir / "git_info.json"
    dataset_metadata_path = dataset_dir / "dataset_metadata.json"

    git_info_path.write_text(
        json.dumps(git_info, indent=2),
        encoding="utf-8",
    )

    dataset_metadata_path.write_text(
        json.dumps(dataset_metadata, indent=2),
        encoding="utf-8",
    )

    return {
        "root": temp_dir,
        "git_info": git_info_path,
        "dataset_metadata": dataset_metadata_path,
        "uv_lock": UV_LOCK_PATH,
    }
