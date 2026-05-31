import os
from turtle import st
import numpy as np

Target_Column = "Result"

Pipeline_Name = "NetworkSecurity"
Artifact_Dir = "Artifacts"

File_Name = "phisingData.csv"

Train_file_name = "Train.csv"
Test_file_name = "Test.csv"

Schema_file_path = os.path.join("data_schema","schema.yaml")
Saved_Model_Dir = ("saved_models")
Model_File_Name = "model.pkl"


#Data Ingestion related constants
Data_Ingestion_Collection_Name = "NetworkSecurityData"
Data_Ingestion_Database_Name = "ChinuAI"

Data_Ingestion_DIR_Name = "Data_Ingestion"
Data_Ingestion_Feature_Store_DIR_Name = "Feature_Store"
Data_Ingestion_Ingested_Name = "Ingested"

Data_Ingestion_Train_Test_Split_Ratio = 0.2

#Data Validation related constants
Data_Validation_DIR_Name : str = "Data_Validation"
Data_Validation_Valid_Dir: str = "Validated"
Data_Validation_InValid_Dir: str = "InValid"
Data_Validation_Drift_Report_Dir: str = "Drift_Report"
Data_Validation_Drift_Report_File_Name: str = "Report.yaml"
Preprocessing_Object_File_Name :str = "preprocessing.pkl"

#Data Transformation related constants
Data_Transformation_Dir_Name: str = "Data_Transformation"
Data_Transformation_Transformed_Data_Dir: str = "transformed"
Data_Transformation_Transformed_Object_Dir: str = "transformed_object"

#Knn imputer to replacenan values with mean of nearest neighbours
Data_Transformation_Imputer_Params: dict ={
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform"
}


Data_Transformation_Train_File_Path : str= "train.py" 

Data_Transformation_Test_File_Path : str= "test.py"

"""
Model Trainer related constants start with Model Trainer Var Name
"""
Model_Trainer_DIR_Name: str = "Model_Trainer"
Model_Trainer_Trained_Model_Dir: str = "trained_model"
Model_Trainer_Trained_Model_Name :str = "model.pkl"
Model_Trainer_Expected_Score : float = 0.6
Model_Trainer_Overfitting_Underfitting_Threshold: float = 0.05


