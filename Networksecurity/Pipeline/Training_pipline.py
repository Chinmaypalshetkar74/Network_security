import sys

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Logging.logger import (
    logging
)

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

from Networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact
)


class TrainPipeline:

    def __init__(self):

        self.training_pipeline_config = (
            trainingPiplineConfig()
        )

    # ==========================================
    # DATA INGESTION
    # ==========================================

    def start_data_ingestion(
        self
    ) -> DataIngestionArtifact:

        try:

            data_ingestion_config = (
                DataIngestionConfig(
                    self.training_pipeline_config
                )
            )

            data_ingestion = (
                DataIngestion(
                    data_ingestion_config
                )
            )

            logging.info(
                "Starting Data Ingestion"
            )

            data_ingestion_artifact = (
                data_ingestion
                .initiate_data_ingestion()
            )

            logging.info(
                "Data Ingestion Completed"
            )

            return (
                data_ingestion_artifact
            )

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )

    # ==========================================
    # DATA VALIDATION
    # ==========================================

    def start_data_validation(
        self,
        data_ingestion_artifact: DataIngestionArtifact
    ) -> DataValidationArtifact:

        try:

            data_validation_config = (
                DataValidationConfig(
                    self.training_pipeline_config
                )
            )

            data_validation = (
                DataValidation(
                    data_ingestion_artifact,
                    data_validation_config
                )
            )

            logging.info(
                "Starting Data Validation"
            )

            data_validation_artifact = (
                data_validation
                .initiate_data_validation()
            )

            logging.info(
                "Data Validation Completed"
            )

            return (
                data_validation_artifact
            )

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )

    # ==========================================
    # DATA TRANSFORMATION
    # ==========================================

    def start_data_transformation(
        self,
        data_validation_artifact: DataValidationArtifact
    ) -> DataTransformationArtifact:

        try:

            data_transformation_config = (
                DataTransformationConfig(
                    self.training_pipeline_config
                )
            )

            data_transformation = (
                DataTransformation(
                    data_validation_artifact,
                    data_transformation_config
                )
            )

            logging.info(
                "Starting Data Transformation"
            )

            data_transformation_artifact = (
                data_transformation
                .initiate_data_transformation()
            )

            logging.info(
                "Data Transformation Completed"
            )

            return (
                data_transformation_artifact
            )

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )

    # ==========================================
    # MODEL TRAINER
    # ==========================================

    def start_model_trainer(
        self,
        data_transformation_artifact: DataTransformationArtifact
    ) -> ModelTrainerArtifact:

        try:

            model_trainer_config = (
                ModelTrainerConfig(
                    self.training_pipeline_config
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

            logging.info(
                "Starting Model Training"
            )

            model_trainer_artifact = (
                model_trainer
                .initiate_model_trainer()
            )

            logging.info(
                "Model Training Completed"
            )

            return (
                model_trainer_artifact
            )

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )

    # ==========================================
    # RUN COMPLETE PIPELINE
    # ==========================================

    def run_pipeline(self):

        try:

            data_ingestion_artifact = (
                self.start_data_ingestion()
            )

            data_validation_artifact = (
                self.start_data_validation(
                    data_ingestion_artifact
                )
            )

            data_transformation_artifact = (
                self.start_data_transformation(
                    data_validation_artifact
                )
            )

            model_trainer_artifact = (
                self.start_model_trainer(
                    data_transformation_artifact
                )
            )

            return (
                model_trainer_artifact
            )

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )