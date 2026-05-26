# for atlas
""" import os
import sys
import json
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

Mongo_db_url = os.getenv("Mongo_db_url")
print(Mongo_db_url)

import certifi
ca=certifi.where()

import pymongo
import pandas as pd
import numpy as np
import networksecurity.exceptions as exception import NetworkSecurityException
from networksecurity.logger import logging

class NetworkSecurityDataExtraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json_converter(self,cv_file_path):
        try:
            data=pd.read_csv(cv_file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json(orient='records')).values())
            return records
        except exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client = pymongo.MongoClient(Mongo_db_url)
            self.database=self.mongo_client[self.database]

            self.collection=self.mongo_client[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    file_path="Network_Data\phisingData.csv"
    DATABASE="ChinuAI"
    COLLECTION="NetworkSecurityData"
    networkjob=NetworkSecurityDataExtraction()
    records=networkjob.csv_to_json_converter(file_path)
    print(records)
    no_of_records=networkjob.insert_data_to_mongodb(records,DATABASE,COLLECTION)
""" 

#for docker mongodb -
import os
import sys
import pandas as pd
import numpy as np
import json
import pymongo

from dotenv import load_dotenv

from Networksecurity.Exception.exception import NetworkSecurityException
from Networksecurity.Logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("Mongo_db_url")


class NetworkSecurityDataExtraction:

    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):

        try:
            data = pd.read_csv(file_path)

            data.reset_index(drop=True, inplace=True)

            records = data.to_dict(orient="records")

            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongodb(self, records, database, collection):

        try:
            db = self.mongo_client[database]

            collection = db[collection]

            collection.insert_many(records)

            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    FILE_PATH = r"Network_Data\phisingData.csv"

    DATABASE = "ChinuAI"

    COLLECTION = "NetworkSecurityData"

    network_obj = NetworkSecurityDataExtraction()

    records = network_obj.csv_to_json_converter(FILE_PATH)

    print(records[:5])

    no_of_records = network_obj.insert_data_to_mongodb(
        records,
        DATABASE,
        COLLECTION
    )

    print(f"{no_of_records} records inserted successfully")