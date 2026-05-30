import os


Target_Column = "Result"

Pipeline_Name = "NetworkSecurity"
Artifact_Dir = "Artifacts"

File_Name = "phisingData.csv"

Train_file_name = "Train.csv"
Test_file_name = "Test.csv"

Schema_file_path = os.path.join("data_schema","schema.yaml")

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