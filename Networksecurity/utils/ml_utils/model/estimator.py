import os
import sys

from Networksecurity.Constants.Training_pipeline import (
    Saved_Model_Dir,
    Model_File_Name
)

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Logging import logger


class NetworkSecurityModel:

    def __init__(
        self,
        preprocessor,
        model
    ):
        try:

            self.preprocessor = preprocessor
            self.model = model

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )

    def predict(
        self,
        X
    ):

        try:

            x_transformed = (
                self.preprocessor
                .transform(X)
            )

            y_hat = (
                self.model
                .predict(x_transformed)
            )

            return y_hat

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )