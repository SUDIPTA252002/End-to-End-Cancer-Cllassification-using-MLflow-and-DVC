from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.Training import Training
import os
from cnnClassifier.exception import CustomException
from cnnClassifier import logger
import sys

STAGE_NAME='Model Training Stage'
class TrainingModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        training_config=config.get_model_trainer_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__=='__main__':
    try:
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=TrainingModelPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")

    except Exception as e:
        raise CustomException(e,sys)