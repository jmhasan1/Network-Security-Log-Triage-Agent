import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL =os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            # below we have unconventional but functional way to transform data, likely from a pandas DataFrame, into a list of dictionaries.
            records=list(json.loads(data.T.to_json()).values())
            # A cleaner, more direct alternative using standard pandas methods is:
            # records = data.to_dict(orient='list')
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def insert_data_mongodb(self, records, database, collection):
        try:
            # Store input parameters as instance attributes (assuming 'self' is part of a class)
            self.database = database
            self.collection = collection
            self.records = records

            # Establish a connection to the MongoDB server using a URL defined elsewhere (MONGO_DB_URL)
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            # Select the target database
            self.database = self.mongo_client[self.database]
        
            # Select the target collection within the database
            self.collection = self.database[self.collection]

            # Insert all documents from the 'records' list into the collection
            self.collection.insert_many(self.records)

            # Return the count of records that were attempted to be inserted
            return (len(self.records))

        except Exception as e:
            # If any error occurs during the process (e.g., connection failure, authentication error)
            # the exception is caught, wrapped in a custom exception (NetworkSecurityException), and raised again.
            raise NetworkSecurityException(e, sys)

        
if __name__ == '__main__':
    FILE_PATH = "data/raw/phisingData.csv"
    DATABASE = "Jahid'sAI"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)

    # print(records)

    no_of_records = networkobj.insert_data_mongodb(
        records,
        DATABASE,
        Collection
    )

    print(no_of_records)