from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.entity.config_entity import PrepBaseModelConfig
from cnnClassifier.components.Base_Model import PrepBaseModel
from cnnClassifier.exception import CustomException
from cnnClassifier import logger
import sys

STAGE_NAME='Preparation of Base Model Stage'
class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        base_model_config=config.prep_base_model_config()
        prep_base_model=PrepBaseModel(config=base_model_config)
        prep_base_model.get_base_model()
        prep_base_model.update_base_model()

STAGE_NAME='Model Training Stage'
if __name__=='__main__':
    try:
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")

    except Exception as e:
        raise CustomException(e,sys)