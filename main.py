from cnnClassifier.exception import CustomException
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prep_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingModelPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
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


STAGE_NAME='Preparation of Base Model Stage'
if __name__=="__main__":
    try:
        logger.info("*******************")
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")

    except Exception as e:
        raise CustomException(e,sys)
    
STAGE_NAME="Model Training Stage"
if __name__=='__main__':
    try:
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=TrainingModelPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")

    except Exception as e:
        raise CustomException(e,sys)
    

STAGE_NAME="Model Evaluation Stage"
if __name__=="__main__":
    try:
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=ModelEvaluationPipeline()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")
        obj.main()
    except Exception as e:
        raise CustomException(e,sys)
