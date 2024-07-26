from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.Data_Ingestion import DataIngestion
from cnnClassifier.exception import CustomException
from cnnClassifier import logger

import sys




STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__=="__main__":
    try:
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")
        pass
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)

