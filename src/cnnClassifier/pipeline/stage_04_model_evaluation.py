from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.Model_Evaluation import Evaluation
from cnnClassifier.exception import CustomException
from cnnClassifier import logger
import sys

STAGE_NAME="MODEL EVALUATION STAGE"
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        evaluation_config=config.get_evaluation_config()
        evaluation=Evaluation(config=evaluation_config)
        evaluation.evaluate()
        evaluation.log_into_mlflow()


if __name__=="__init__":
    try:
        logger.info(f">>>stage {STAGE_NAME} started")
        obj=ModelEvaluationPipeline()
        logger.info(f">>>stage {STAGE_NAME} completed")
        logger.info("x================x")
        obj.main()
    except Exception as e:
        raise CustomException(e,sys)
