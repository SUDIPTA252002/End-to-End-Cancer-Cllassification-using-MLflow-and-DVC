import mlflow.keras
import tensorflow as tf
from cnnClassifier.utils.common import save_json
from urllib.parse import urlparse
import mlflow
import mlflow.keras
from cnnClassifier.entity.config_entity import EvaluationConfig
from pathlib import Path

class Evaluation:
    def __init__(self,config=EvaluationConfig):
        self.config=config
    
    def valid_generator(self):
        datagenerator_kwargs=dict(
            rescale=1./255,
            validation_split=0.30
        )

        dataflow_kwargs=dict(
            target_size=self.config.image_size[:-1],
            batch_size=self.config.batch_size,
            interpolation='bilinear'
        )

        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_datagenerator=valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            shuffle=False,
            subset='validation',
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path:Path)->tf.keras.Model:
        model=tf.keras.models.load_model(path)
        return model
        
    def evaluate(self):
        self.model=self.load_model(self.config.path_of_model)
        self.valid_generator()
        self.score=self.model.evaluate(self.valid_datagenerator)
        self.save_score()

    def save_score(self):
        scores={
                "loss":self.score[0],
                "accuarcy":self.score[1]
            }
        save_json(path=Path("scores.json"),data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({
                    "loss":self.score[0],
                    "accuracy":self.score[1]
                })
            if tracking_url_type_store!='file':
                mlflow.keras.log_model(self.model,"model",registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model,"model")
            
