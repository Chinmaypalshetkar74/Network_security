from Networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)

from Networksecurity.entity.config_entity import (
    DataValidationConfig
)

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Constants.Training_pipeline import (
    Schema_file_path
)

from Networksecurity.Logging.logger import logging

from scipy.stats import ks_2samp

import pandas as pd
import os
import sys

from Networksecurity.utils.main_utils.utils import (
    read_yaml_file,
    write_yaml_file
)


class DataValidation:

    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
    ):

        try:

            self.data_ingestion_artifact = (
                data_ingestion_artifact
            )

            self.data_validation_config = (
                data_validation_config
            )

            self._schema_config = read_yaml_file(
                Schema_file_path
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:

        try:

            return pd.read_csv(file_path)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_number_of_columns(
        self,
        dataframe: pd.DataFrame
    ) -> bool:

        try:

            number_of_columns = len(
                self._schema_config["columns"]
            )

            logging.info(
                f"Required columns: {number_of_columns}"
            )

            logging.info(
                f"Available columns: {len(dataframe.columns)}"
            )

            if len(dataframe.columns) == number_of_columns:
                return True

            return False

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_data_drift(
        self,
        base_df,
        current_df,
        threshold=0.05
    ):

        try:

            status = True

            report = {}

            for column in base_df.columns:

                d1 = base_df[column]

                d2 = current_df[column]

                ks_test = ks_2samp(d1, d2)

                if ks_test.pvalue < threshold:
                    drift_found = True
                    status = False
                else:
                    drift_found = False

                report[column] = {
                    "p_value": float(ks_test.pvalue),
                    "drift_status": drift_found
                }

            drift_report_file_path = (
                self.data_validation_config
                .drift_report_file_path
            )

            os.makedirs(
                os.path.dirname(
                    drift_report_file_path
                ),
                exist_ok=True
            )

            write_yaml_file(
                file_path=drift_report_file_path,
                content=report
            )

            return status

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(
        self
    ) -> DataValidationArtifact:

        try:

            train_file_path = (
                self.data_ingestion_artifact
                .trained_file_path
            )

            test_file_path = (
                self.data_ingestion_artifact
                .test_file_path
            )

            train_dataframe = self.read_data(
                train_file_path
            )

            test_dataframe = self.read_data(
                test_file_path
            )

            train_status = (
                self.validate_number_of_columns(
                    train_dataframe
                )
            )

            test_status = (
                self.validate_number_of_columns(
                    test_dataframe
                )
            )

            if not train_status:
                raise Exception(
                    "Train dataframe schema mismatch"
                )

            if not test_status:
                raise Exception(
                    "Test dataframe schema mismatch"
                )

            drift_status = (
                self.detect_data_drift(
                    base_df=train_dataframe,
                    current_df=test_dataframe
                )
            )

            os.makedirs(
                os.path.dirname(
                    self.data_validation_config
                    .valid_train_file_path
                ),
                exist_ok=True
            )

            train_dataframe.to_csv(
                self.data_validation_config
                .valid_train_file_path,
                index=False,
                header=True
            )

            test_dataframe.to_csv(
                self.data_validation_config
                .valid_test_file_path,
                index=False,
                header=True
            )

            data_validation_artifact = (
                DataValidationArtifact(
                    validation_status=drift_status,
                    valid_train_file_path=
                    self.data_validation_config
                    .valid_train_file_path,

                    valid_test_file_path=
                    self.data_validation_config
                    .valid_test_file_path,

                    invalid_train_file_path=
                    self.data_validation_config
                    .invalid_train_file_path,

                    invalid_test_file_path=
                    self.data_validation_config
                    .invalid_test_file_path,

                    drift_report_file_path=
                    self.data_validation_config
                    .drift_report_file_path
                )
            )

            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)