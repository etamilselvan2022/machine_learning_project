from housing.logger import logging
from housing.exception import HousingException
import os,sys
#i/p:
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact

class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,
                      data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def is_train_test_file_exists(self):
        try:
            is_train_file_exist=False
            is_test_file_exist=False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exists(train_file_path)
            is_test_file_exist=os.path.exists(test_file_path)

            return is_train_file_exist and is_test_file_exist

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def initiate_data_validation(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e