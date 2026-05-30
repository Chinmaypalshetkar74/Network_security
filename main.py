import sys

from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.components.data_validation import DataValidation

from Networksecurity.entity.config_entity import (
    trainingPiplineConfig,
    DataIngestionConfig,
    DataValidationConfig
)

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Logging.logger import logging


if __name__ == "__main__":

    try:

        # ==========================
        # Training Pipeline Config
        # ==========================

        training_pipeline_config = (
            trainingPiplineConfig()
        )

        # ==========================
        # Data Ingestion
        # ==========================

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

        data_ingestion_artifact = (
            data_ingestion
            .initiate_data_ingestion()
        )

        print(data_ingestion_artifact)

        logging.info(
            "Data Ingestion Completed"
        )

        # ==========================
        # Data Validation
        # ==========================

        data_validation_config = (
            DataValidationConfig(
                training_pipeline_config
            )
        )

        data_validation = DataValidation(
            data_ingestion_artifact,
            data_validation_config
        )

        logging.info(
            "Starting Data Validation"
        )

        data_validation_artifact = (
            data_validation
            .initiate_data_validation()
        )

        print(data_validation_artifact)

        logging.info(
            "Data Validation Completed"
        )

    except Exception as e:

        raise NetworkSecurityException(
            e,
            sys
        )