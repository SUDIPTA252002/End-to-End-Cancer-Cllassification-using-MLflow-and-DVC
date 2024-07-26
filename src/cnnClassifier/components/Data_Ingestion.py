    
from cnnClassifier.constants import *

import os
from cnnClassifier.entity.config_entity import DataIngestionConfig
import gdown
from cnnClassifier import logger
import sys
import zipfile
from cnnClassifier.exception import CustomException 


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self)->str:
        try:
            dataset_url=self.config.source_url
            zip_download_dir=self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)

            file_id=dataset_url.split("/")[-2]
            prefix="https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Data is downloaded from {dataset_url} into {zip_download_dir}")
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def extract_zip_file(self):
        try:
            unzip_path=self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
                zip_ref.extractall(unzip_path)
            pass
        except Exception as e:
            raise CustomException(e,sys)