import os
import sys
from dotenv import load_dotenv

from network_security.utils.lineage import (
    collect_lineage,
    create_lineage_artifacts,
)

from network_security.exception.exception import NetworkSecurityException 
from network_security.logging.logger import logging

from network_security.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from network_security.entity.config_entity import ModelTrainerConfig

from network_security.utils.ml_utils.model.estimator import NetworkModel
from network_security.utils.main_utils.utils import save_object,load_object
from network_security.utils.main_utils.utils import load_numpy_array_data,evaluate_models
from network_security.utils.ml_utils.metric.classification_metric import get_classification_score

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
import mlflow
from urllib.parse import urlparse

import dagshub
# dagshub.init(repo_owner='jmhasan1', repo_name='Network-Security-Log-Triage-Agent', mlflow=True)

load_dotenv()

os.environ["MLFLOW_TRACKING_USERNAME"]=os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"]=os.getenv("MLFLOW_TRACKING_PASSWORD")


class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    # ==========================================================
    # Configure MLflow tracking server (DagsHub)
    # ==========================================================

    def track_mlflow(
        self,
        best_model,
        best_model_name,
        train_metric,
        test_metric,
        train_size,
        test_size,
        model_params=None):

        """
            Log the complete training experiment to MLflow.
        
            Logs
            -----
            • Train metrics
            • Test metrics
            • Hyperparameters
            • Model metadata
            • Registered model (DagsHub)
        
            Returns
            -------
             None
        """

        try:

            mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

            if not mlflow_tracking_uri:
                raise NetworkSecurityException(
                    "MLFLOW_TRACKING_URI is not configured in the environment."
                )

            mlflow.set_tracking_uri(mlflow_tracking_uri)
            
            tracking_scheme = urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():

                # ===========================================
                # Collect experiment lineage & artifacts
                # ===========================================

                lineage = collect_lineage()
                lineage_artifacts = create_lineage_artifacts(lineage)

                mlflow.set_tags(
                {
                    "project_name": lineage["project_name"],
                    "project_version": lineage["project_version"],
                    "git_commit": lineage["git_commit"],
                    "git_branch": lineage["git_branch"],
                    "dataset_version": lineage["dataset_version"],
                    "dataset_dvc_hash": lineage["dataset_dvc_hash"],
                    "dataset_sha256": lineage["dataset_sha256"],
                    "feature_version": lineage["feature_version"],
                    "preprocessing_version": lineage["preprocessing_version"],
                    "python_version": lineage["python_version"],
                    "environment_manager": lineage["environment_manager"],
                    "lockfile_hash": lineage["lockfile_hash"],
                }
                )

                mlflow.log_artifact(
                    str(lineage_artifacts["git_info"]),
                    artifact_path="provenance",
                )

                mlflow.log_artifact(
                    str(lineage_artifacts["dataset_metadata"]),
                    artifact_path="dataset",
                )

                mlflow.log_artifact(
                    str(lineage_artifacts["uv_lock"]),
                    artifact_path="environment",
                )

                # ===========================
                # Training Metrics
                # ===========================

                mlflow.log_metric(
                    "train_f1_score",
                    train_metric.f1_score
                )

                mlflow.log_metric(
                    "train_precision",
                    train_metric.precision_score
                )

                mlflow.log_metric(
                "train_recall",
                train_metric.recall_score
                )

                # ===========================
                # Testing Metrics
                # ===========================

                mlflow.log_metric(
                    "test_f1_score",
                    test_metric.f1_score
                )

                mlflow.log_metric(
                    "test_precision",
                    test_metric.precision_score
                )

                mlflow.log_metric(
                    "test_recall",
                    test_metric.recall_score
                )

                # ===========================================
                # Log model hyperparameters
                # Helps reproduce experiments later
                # ===========================================
                
                if model_params:
                    mlflow.log_params(model_params)

                # ===========================================
                # Log dataset information
                # Helps compare experiments trained on
                # different dataset sizes.
                #===========================================

                mlflow.log_param("train_samples", train_size)
                mlflow.log_param("test_samples", test_size)

                # ===========================================
                # Log metadata
                # ===========================================

                mlflow.set_tag(
                    "model_type",
                    type(best_model).__name__
                )

                # Log selected algorithm
                # Useful for comparing different models across experiments.

                mlflow.log_param(
                    "algorithm",
                    best_model_name
                )

                mlflow.set_tag(
                    "framework",
                    "scikit-learn"
                )

                # log dataset version
                mlflow.set_tag(
                    "dataset_name",
                    "Network Security Phishing Dataset"
                )

                # experiment description
                mlflow.set_tag(
                    "experiment_type",
                    "Baseline Model"
                )

                # ==========================================================
                # Log trained model to the MLflow Tracking Server.
                #
                # If a remote tracking server (DagsHub) is used,
                # also register the model in the MLflow Model Registry.
                #
                # For a local file store, only the model artifact is saved.
                # ==========================================================

                kwargs = {

                    "sk_model": best_model,

                    "name": "model"

                }

                if tracking_scheme != "file":

                    kwargs["registered_model_name"] = "NetworkSecurityLogTriage"

                mlflow.sklearn.log_model(**kwargs)


        except Exception as e:
            logging.warning(
                f"MLflow logging failed: {e}"
                )


        
    def train_model(self,X_train,y_train ,x_test,y_test):

        models = {
                "Random Forest": RandomForestClassifier(verbose=1),
                "Decision Tree": DecisionTreeClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(verbose=1),
                "Logistic Regression": LogisticRegression(verbose=1),
                "AdaBoost": AdaBoostClassifier(),
            }
        
        params={
            "Decision Tree": {
                'criterion':['gini', 'entropy', 'log_loss'],
                # 'splitter':['best','random'],
                # 'max_features':['sqrt','log2'],
            },
            "Random Forest":{
                # 'criterion':['gini', 'entropy', 'log_loss'],
                
                # 'max_features':['sqrt','log2',None],
                'n_estimators': [8,16,32,128,256]
            },
            "Gradient Boosting":{
                # 'loss':['log_loss', 'exponential'],
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.85,0.9],
                # 'criterion':['squared_error', 'friedman_mse'],
                # 'max_features':['auto','sqrt','log2'],
                'n_estimators': [8,16,32,64,128,256]
            },
            "Logistic Regression":{},
            "AdaBoost":{
                'learning_rate':[.1,.01,.001],
                'n_estimators': [8,16,32,64,128,256]
            }
            
        }
        model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=x_test,y_test=y_test,
                                          models=models,param=params)
        
        ## To get best model score from dict
        best_model_score = max(sorted(model_report.values()))

        ## To get best model name from dict

        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        best_model = models[best_model_name]
        y_train_pred=best_model.predict(X_train)

        classification_train_metric=get_classification_score(y_true=y_train,y_pred=y_train_pred)

        y_test_pred=best_model.predict(x_test)
        classification_test_metric=get_classification_score(y_true=y_test,y_pred=y_test_pred)

        # ===========================================
        # Log entire experiment
        # (single MLflow run)
        # ===========================================

        self.track_mlflow(

            best_model=best_model,

            best_model_name=best_model_name,

            train_metric=classification_train_metric,

            test_metric=classification_test_metric,

            train_size=len(X_train),

            test_size=len(x_test),

            model_params=best_model.get_params()

        )

        preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            
        model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_path,exist_ok=True)

        network_model = NetworkModel(preprocessor=preprocessor,
                                     model=best_model)
        save_object(self.model_trainer_config.trained_model_file_path,
                    obj=network_model)
        #model pusher
        save_object("models/model.pkl",best_model)

        ## Model Trainer Artifact
        model_trainer_artifact=ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                             train_metric_artifact=classification_train_metric,
                             test_metric_artifact=classification_test_metric
                             )
        logging.info(f"Model trainer artifact: {model_trainer_artifact}")
        return model_trainer_artifact
    
        
    
    # Initiate model trainer 
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            #loading training array and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            model_trainer_artifact=self.train_model(x_train,y_train,x_test,y_test)
            return model_trainer_artifact
        

        except Exception as e:
            raise NetworkSecurityException(e,sys)


