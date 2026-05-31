import os
import sys

from Networksecurity.Exception.exception import NetworkSecurityException

from Networksecurity.Logging.logger import logging
from Networksecurity.entity.config_entity import ModelTrainerConfig
from Networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact
)

from Networksecurity.utils.ml_utils.model.estimator import (
    NetworkSecurityModel
)

from Networksecurity.utils.main_utils.utils import (
    save_object,
    load_object,
    load_numpy_array_data,
    evaluate_models
)

from Networksecurity.utils.ml_utils.metric.classification_metric import (
    get_classification_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)


class ModelTrainer:

    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        datatransformation_artifact: DataTransformationArtifact
    ):
        try:
            self.model_trainer_config = model_trainer_config
            self.datatransformation_artifact = (
                datatransformation_artifact
            )

        except Exception as e:
            raise NetworkSecurityException(
                e,
                sys
            )

    def train_model(
        self,
        x_train,
        y_train,
        x_test,
        y_test
    ):

        try:

            models = {
                "Logistic Regression":
                    LogisticRegression(verbose=1),

                "KNN":
                    KNeighborsClassifier(),

                "Decision Tree":
                    DecisionTreeClassifier(),

                "Random Forest":
                    RandomForestClassifier(
                        verbose=1
                    ),

                "AdaBoost":
                    AdaBoostClassifier(),

                "Gradient Boosting":
                    GradientBoostingClassifier(
                        verbose=1
                    )
            }

            params = {

                "Logistic Regression": {
                    "C": [0.1, 0.5, 1.0, 5.0, 10.0],
                    "solver": [
                        "liblinear",
                        "lbfgs"
                    ]
                },

                "KNN": {
                    "n_neighbors": [3, 5, 7, 9],
                    "weights": [
                        "uniform",
                        "distance"
                    ]
                },

                "Decision Tree": {
                    "criterion": [
                        "gini",
                        "entropy"
                    ],
                    "max_depth": [
                        None,
                        10,
                        20,
                        30
                    ]
                },

                "Random Forest": {
                    "n_estimators": [
                        100,
                        200
                    ],
                    "max_depth": [
                        None,
                        10,
                        20
                    ]
                },

                "AdaBoost": {
                    "n_estimators": [
                        50,
                        100
                    ],
                    "learning_rate": [
                        0.01,
                        0.1
                    ]
                },

                "Gradient Boosting": {
                    "n_estimators": [
                        100,
                        200
                    ],
                    "learning_rate": [
                        0.01,
                        0.1
                    ]
                }
            }

            model_report = evaluate_models(
            X_train=x_train,
            y_train=y_train,
            X_test=x_test,
            y_test=y_test,
            models=models,
            param=params
         )

            best_model_score = max(
                sorted(
                    model_report.values()
                )
            )

            best_model_name = list(
                model_report.keys()
            )[
                list(
                    model_report.values()
                ).index(
                    best_model_score
                )
            ]

            best_model = models[
                best_model_name
            ]

            y_train_pred = (
                best_model.predict(
                    x_train
                )
            )

            classification_train_metric = (
                get_classification_score(
                    y_true=y_train,
                    y_pred=y_train_pred
                )
            )

            y_test_pred = (
                best_model.predict(
                    x_test
                )
            )

            classification_test_metric = (
                get_classification_score(
                    y_true=y_test,
                    y_pred=y_test_pred
                )
            )

            preprocessing_obj = load_object(
            file_path=
            self.datatransformation_artifact
            .transformed_object_file_path
     )

            model_dir_path = (
                os.path.dirname(
                    self.model_trainer_config
                    .trained_model_file_path
                )
            )

            os.makedirs(
                model_dir_path,
                exist_ok=True
            )

            network_security_model = (
            NetworkSecurityModel(
            preprocessor=
            preprocessing_obj,

            model=
            best_model
            )
        )

            save_object(
                file_path=
                self.model_trainer_config
                .trained_model_file_path,

                obj=
                network_security_model
            )

            model_trainer_artifact = (
                ModelTrainerArtifact(
                    trained_model_file_path=
                    self.model_trainer_config
                    .trained_model_file_path,

                    train_metric_artifact=
                    classification_train_metric,

                    test_metric_artifact=
                    classification_test_metric
                )
            )

            logging.info(
                f"Model trainer artifact: "
                f"{model_trainer_artifact}"
            )

            return (
                model_trainer_artifact
            )

        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )

    def initiate_model_trainer(
        self
    ) -> ModelTrainerArtifact:

        try:

            train_file_path = (
                self.datatransformation_artifact
                .transformed_train_file_path
            )

            test_file_path = (
                self.datatransformation_artifact
                .transformed_test_file_path
            )

            train_array = (
                load_numpy_array_data(
                    train_file_path
                )
            )

            test_array = (
                load_numpy_array_data(
                    test_file_path
                )
            )

            x_train = (
                train_array[:, :-1]
            )

            y_train = (
                train_array[:, -1]
            )

            x_test = (
                test_array[:, :-1]
            )

            y_test = (
                test_array[:, -1]
            )

            model_trainer_artifact = (
                self.train_model(
                    x_train,
                    y_train,
                    x_test,
                    y_test
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
        

