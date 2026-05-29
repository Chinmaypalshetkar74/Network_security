import sys

from Networksecurity.components.data_ingestion import DataIngestion

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Logging.logger import logging

from Networksecurity.entity.config_entity import (
    trainingPiplineConfig,
    DataIngestionConfig
)


if __name__ == "__main__":

    try:

        training_pipeline_config = (
            trainingPiplineConfig()
        )

        data_ingestion_config = (
            DataIngestionConfig(
                training_pipeline_config
            )
        )

        data_ingestion = DataIngestion(
            data_ingestion_config
        )

        logging.info(
            "Starting Data Ingestion"
        )

        artifact = (
            data_ingestion
            .initiate_data_ingestion()
        )

        print(artifact)

        logging.info(
            "Data Ingestion Completed"
        )

    except Exception as e:

        raise NetworkSecurityException(
            e,
            sys
        )