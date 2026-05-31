import sys

from Networksecurity.components.data_ingestion import (
    DataIngestion
)

from Networksecurity.components.data_validation import (
    DataValidation
)

from Networksecurity.components.data_transformation import (
    DataTransformation
)

from Networksecurity.components.Model_Trainer import (
    ModelTrainer
)

from Networksecurity.entity.config_entity import (
    trainingPiplineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Logging.logger import (
    logging
)


if __name__ == "__main__":

    try:

        # =====================================
        # Training Pipeline Config
        # =====================================

        training_pipeline_config = (
            trainingPiplineConfig()
        )

        # =====================================
        # Data Ingestion
        # =====================================

        logging.info(
            "Starting Data Ingestion"
        )

        data_ingestion_config = (
            DataIngestionConfig(
                training_pipeline_config
            )
        )

        data_ingestion = DataIngestion(
            data_ingestion_config
        )

        data_ingestion_artifact = (
            data_ingestion
            .initiate_data_ingestion()
        )

        print(
            data_ingestion_artifact
        )

        logging.info(
            "Data Ingestion Completed"
        )

        # =====================================
        # Data Validation
        # =====================================

        logging.info(
            "Starting Data Validation"
        )

        data_validation_config = (
            DataValidationConfig(
                training_pipeline_config
            )
        )

        data_validation = DataValidation(
            data_ingestion_artifact,
            data_validation_config
        )

        data_validation_artifact = (
            data_validation
            .initiate_data_validation()
        )

        print(
            data_validation_artifact
        )

        logging.info(
            "Data Validation Completed"
        )

        # =====================================
        # Data Transformation
        # =====================================

        logging.info(
            "Starting Data Transformation"
        )

        data_transformation_config = (
            DataTransformationConfig(
                training_pipeline_config
            )
        )

        data_transformation = (
            DataTransformation(
                data_validation_artifact,
                data_transformation_config
            )
        )

        data_transformation_artifact = (
            data_transformation
            .initiate_data_transformation()
        )

        print(
            data_transformation_artifact
        )

        logging.info(
            "Data Transformation Completed"
        )

        # =====================================
        # Model Training
        # =====================================

        logging.info(
            "Starting Model Training"
        )

        model_trainer_config = (
            ModelTrainerConfig(
                training_pipeline_config
            )
        )

        model_trainer = (
            ModelTrainer(
                model_trainer_config=
                model_trainer_config,

                datatransformation_artifact=
                data_transformation_artifact
            )
        )

        model_trainer_artifact = (
            model_trainer
            .initiate_model_trainer()
        )

        print(
            model_trainer_artifact
        )

        logging.info(
            "Model Training Completed"
        )

    except Exception as e:

        raise NetworkSecurityException(
            e,
            sys
        )