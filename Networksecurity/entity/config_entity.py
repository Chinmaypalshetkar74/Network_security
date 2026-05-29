from datetime import datetime
import os

from Networksecurity.Constants import Training_pipeline


class trainingPiplineConfig:

    def __init__(self, timestamp=None):

        if timestamp is None:
            timestamp = datetime.now()

        timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")

        self.pipeline_name = Training_pipeline.Pipeline_Name

        self.artifact_name = Training_pipeline.Artifact_Dir

        self.artifact_dir = os.path.join(
            self.artifact_name,
            timestamp
        )

        self.timestamp = timestamp


class DataIngestionConfig:

    def __init__(self,
                 training_pipline_config: trainingPiplineConfig):

        self.data_ingestion_dir = os.path.join(
            training_pipline_config.artifact_dir,
            Training_pipeline.Data_Ingestion_DIR_Name
        )

        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            Training_pipeline.Data_Ingestion_Feature_Store_DIR_Name,
            Training_pipeline.File_Name
        )

        self.training_file_path = os.path.join(
            self.data_ingestion_dir,
            Training_pipeline.Data_Ingestion_Ingested_Name,
            Training_pipeline.Train_file_name
        )

        self.test_file_path = os.path.join(
            self.data_ingestion_dir,
            Training_pipeline.Data_Ingestion_Ingested_Name,
            Training_pipeline.Test_file_name
        )

        self.train_test_split_ratio = (
            Training_pipeline.Data_Ingestion_Train_Test_Split_Ratio
        )

        self.collection_name = (
            Training_pipeline.Data_Ingestion_Collection_Name
        )

        self.database_name = (
            Training_pipeline.Data_Ingestion_Database_Name
        )