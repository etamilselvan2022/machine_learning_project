from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging
import os,sys




class Configuration:

    def __init__(self,
                 config_file_path:str=CONFIG_FILE_PATH,
                 current_time_stamp:str=CURRENT_TIME_STAMP) ->None:
        try:
            self.config_info=read_yaml_file(file_path=config_file_path)
            self.time_stamp=current_time_stamp
            self.traning_pipeline_config=self.get_training_pipeline_config()
           #### self.data_ingestion_config=self.get_data_ingestion_config()
            
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir=self.traning_pipeline_config.artifact_dir

            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]

            data_ingestion_artifact_dir=os.path.join(artifact_dir,
                                                     DATA_INGESTION_ARTIFACT_DIR,
                                                     self.time_stamp
                                                     )
           
            dataset_download_url=data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            tgz_download_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            
            ingested_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_train_dir=os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir=os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            logging.info(f"dataset_download_url:{dataset_download_url}")
            logging.info(f"tgz_download_dir:{tgz_download_dir}")
            logging.info(f"raw_data_dir:{raw_data_dir}")
            logging.info(f"ingested_train_dir:{ingested_train_dir}")
            logging.info(f"ingested_test_dir:{ingested_test_dir}")
            
            data_ingestion_config=DataIngestionConfig(dataset_download_url=dataset_download_url, 
                                                      tgz_download_dir=tgz_download_dir, 
                                                      raw_data_dir=raw_data_dir, 
                                                      ingested_train_dir=ingested_train_dir, 
                                                      ingested_test_dir=ingested_test_dir)
            logging.info(f"data_ingestion_config:{data_ingestion_config}")                                                                  
            return data_ingestion_config                                                   
        except Exception as e:
            raise HousingException(e,sys) from e    

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir=self.traning_pipeline_config.artifact_dir

            data_validation_artifact_dir=os.path.join(artifact_dir,
                                                     DATA_VALIDATION_ARTIFACT_DIR_NAME,
                                                     self.time_stamp
                                                     )
            data_validation_info=self.config_info[DATA_VALIDATION_CONFIG_KEY]                                     
            
            #Schema File Path:                                                     
            schema_file_path=os.path.join(ROOT_DIR,
                                          data_validation_info[DATA_VALIDATION_SCHEMA_DIR_KEY],
                                          data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY])

            #Report File Path:
            report_file_path=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY])

            #Report Page File path: 
            report_page_file_path=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])


            data_validation_config=DataValidationConfig(schema_file_path=schema_file_path
                                                        ,report_file_path=report_file_path
                                                        ,report_page_file_path=report_page_file_path)

            return data_validation_config                                                        
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            pipeline_name=training_pipeline_config[TRAINING_PIPELINE_NAME_KEY]
            artifact_dir_name=training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            artifact_dir=os.path.join(ROOT_DIR,pipeline_name,artifact_dir_name)
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Config:{training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e    