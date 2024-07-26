from cnnClassifier.exception import CustomException
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
import sys

STAGE_NAME="Data Ingestion Stage"


if __name__=="__main__":
    try:
        logger.info("x================x")
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")
        pass
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)
