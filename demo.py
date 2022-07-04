from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_validation import DataValidation
from housing.component.data_ingestion import DataIngestion

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
        #data_ingestion_artifact=DataIngestion(Configuration().get_data_ingestion_config()).initiate_data_ingestion()
        #data_validation_config=Configuration().get_data_validation_config()
        #val=DataValidation(data_validation_config,data_ingestion_artifact).is_train_test_file_exists()
        #print(f"data_validation_config:{data_validation_config}")
        #print(f"\n \n data_ingestion_artifact:{data_ingestion_artifact}")
        #print(val)
    except Exception as e:
        logging.error(f'{e}')
        print(e)




if __name__=="__main__":
    main()    