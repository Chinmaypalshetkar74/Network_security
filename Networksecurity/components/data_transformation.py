import logging
import sys
import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from Networksecurity.Constants.Training_pipeline import (
    Target_Column,
    Data_Transformation_Imputer_Params
)

from Networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact
)

from Networksecurity.entity.config_entity import (
    DataTransformationConfig
)

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.utils.main_utils.utils import (
    save_numpy_array_data,
    save_object
)


class DataTransformation:

    def __init__(
        self,
        data_validation_artifact: DataValidationArtifact,
        data_transformation_config: DataTransformationConfig
    ):
        try:

            self.data_validation_artifact = (
                data_validation_artifact
            )

            self.data_transformation_config = (
                data_transformation_config
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:

        try:
            return pd.read_csv(file_path)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def get_data_transformer_object(self) -> Pipeline:
        """
        Create preprocessing pipeline.
        """

        logging.info(
            "Entered get_data_transformer_object method"
        )

        try:

            imputer = KNNImputer(
                **Data_Transformation_Imputer_Params
            )

            logging.info(
                f"KNNImputer initialized with "
                f"{Data_Transformation_Imputer_Params}"
            )

            processor = Pipeline(
                [
                    ("KNNImputer", imputer)
                ]
            )

            return processor

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_transformation(
        self
    ) -> DataTransformationArtifact:

        logging.info(
            "Entered initiate_data_transformation method"
        )

        try:

            logging.info(
                "Starting Data Transformation"
            )

            train_df = self.read_data(
                self.data_validation_artifact
                .valid_train_file_path
            )

            test_df = self.read_data(
                self.data_validation_artifact
                .valid_test_file_path
            )

            # ==========================
            # Train Dataset
            # ==========================

            input_feature_train_df = train_df.drop(
                columns=[Target_Column],
                axis=1
            )

            target_feature_train_df = train_df[
                Target_Column
            ]

            target_feature_train_df = (
                target_feature_train_df
                .replace(-1, 0)
            )

            # ==========================
            # Test Dataset
            # ==========================

            input_feature_test_df = test_df.drop(
                columns=[Target_Column],
                axis=1
            )

            target_feature_test_df = test_df[
                Target_Column
            ]

            target_feature_test_df = (
                target_feature_test_df
                .replace(-1, 0)
            )

            # ==========================
            # Preprocessing
            # ==========================

            preprocessor = (
                self.get_data_transformer_object()
            )

            preprocessor_object = (
                preprocessor.fit(
                    input_feature_train_df
                )
            )

            transformed_input_train_feature = (
                preprocessor_object.transform(
                    input_feature_train_df
                )
            )

            transformed_input_test_feature = (
                preprocessor_object.transform(
                    input_feature_test_df
                )
            )

            train_arr = np.c_[
                transformed_input_train_feature,
                np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                transformed_input_test_feature,
                np.array(target_feature_test_df)
            ]

            # ==========================
            # Save Arrays
            # ==========================

            save_numpy_array_data(
                self.data_transformation_config
                .transformed_train_file_path,
                array=train_arr
            )

            save_numpy_array_data(
                self.data_transformation_config
                .transformed_test_file_path,
                array=test_arr
            )

            save_object(
                self.data_transformation_config
                .transformed_object_file_path,
                preprocessor_object
            )

            save_object( "Final_models/preprocessor.pkl", preprocessor_object )

            # ==========================
            # Artifact
            # ==========================

            data_transformation_artifact = (
                DataTransformationArtifact(
                    transformed_object_file_path=
                    self.data_transformation_config
                    .transformed_object_file_path,

                    transformed_train_file_path=
                    self.data_transformation_config
                    .transformed_train_file_path,

                    transformed_test_file_path=
                    self.data_transformation_config
                    .transformed_test_file_path
                )
            )

            logging.info(
                "Data Transformation Completed"
            )

            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)