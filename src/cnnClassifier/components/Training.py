import tensorflow as tf
from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path

import tensorflow as tf
class Training:
    def __init__(self,config=TrainingConfig):
        self.config=config

    def get_base_model(self):
        self.model=tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self):
        datagenerator_kwargs=dict(
            rescale= 1./255,
            validation_split=0.20
       )
        
        dataflow_kwargs=dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )

        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_datagenerator=valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_augmented:
            train_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )

        else:
            train_datagenerator=valid_datagenerator

        self.train_datagenerator=train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    def train(self):
        self.step_per_epochs=self.train_datagenerator.samples//self.train_datagenerator.batch_size
        self.validation_steps=self.valid_datagenerator.samples//self.valid_datagenerator.batch_size

        early_Stopping=tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            min_delta=0.001,
            patience=3,
            verbose=1,
            mode='auto'
        )
        self.model.fit(self.train_datagenerator,
                       epochs=self.config.params_epochs,
                       steps_per_epoch=self.step_per_epochs,
                       validation_data=self.valid_datagenerator,
                       validation_steps=self.validation_steps,
                       callbacks=[early_Stopping]
                       )
        
        self.save_model(path=self.config.trained_model_path,model=self.model)

        
    @staticmethod
    def save_model(path:Path,model:tf.keras.models):
        model.save(str(path))

        