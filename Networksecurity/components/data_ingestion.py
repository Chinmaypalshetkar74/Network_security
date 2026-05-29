from Networksecurity.Exception.exception import NetworkSecurityException
from Networksecurity.Logging.logger import logging
from Networksecurity.entity.artifact_entity import DataIngestionArtifact

from Networksecurity.entity.config_entity import DataIngestionConfig

import os
import sys
import pymongo
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:

    def __init__(
        self,
        data_ingestion_config: DataIngestionConfig
    ):
        try:
            self.data_ingestion_config = data_ingestion_config

            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_collection_as_dataframe(self):

        try:

            database_name = (
                self.data_ingestion_config.database_name
            )

            collection_name = (
                self.data_ingestion_config.collection_name
            )

            collection = (
                self.mongo_client
                [database_name]
                [collection_name]
            )

            df = pd.DataFrame(
                list(collection.find())
            )

            if "_id" in df.columns:
                df.drop(
                    columns=["_id"],
                    inplace=True
                )

            df.replace(
                {"na": np.nan},
                inplace=True
            )

            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_into_feature_store(
            self,
            dataframe: pd.DataFrame):

        try:

            file_path = (
                self.data_ingestion_config
                .feature_store_file_path
            )

            os.makedirs(
                os.path.dirname(file_path),
                exist_ok=True
            )

            dataframe.to_csv(
                file_path,
                index=False,
                header=True
            )

            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test(
            self,
            dataframe: pd.DataFrame):

        try:

            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config
                .train_test_split_ratio,
                random_state=42
            )

            os.makedirs(
                os.path.dirname(
                    self.data_ingestion_config
                    .training_file_path
                ),
                exist_ok=True
            )

            train_set.to_csv(
                self.data_ingestion_config
                .training_file_path,
                index=False
            )

            test_set.to_csv(
                self.data_ingestion_config
                .test_file_path,
                index=False
            )

            logging.info(
                "Train/Test split completed"
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):

        try:

            dataframe = (
                self.export_collection_as_dataframe()
            )

            dataframe = (
                self.export_data_into_feature_store(
                    dataframe
                )
            )

            self.split_data_as_train_test(
                dataframe
            )

            data_ingestion_artifact = (
                DataIngestionArtifact(
                    trained_file_path=
                    self.data_ingestion_config
                    .training_file_path,

                    test_file_path=
                    self.data_ingestion_config
                    .test_file_path
                )
            )

            return data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)


        

   


       