import os
import sys
from cnnClassifier import logger
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
import yaml
import joblib
import json
from pathlib import Path
from typing import Any
import base64
from cnnClassifier.exception import CustomException

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml)
            logger.info(f"yaml file:{path_to_yaml} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
        logger.info(f"json file saves at:{path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"JSON file loaded successfullt on:{path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at path:{path}")

@ensure_annotations
def load_bin(path:Path):
    joblib.load(path)
    logger.info(f"File loaded from:{path}")

def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path))
    return f"~(size_in_kb)KB"

def decodeImage(imgString,fileName):
    imgdata=base64.b64decode(imgString)
    with open(fileName,"wb") as f:
        f.write(imgdata)
        f.close()

def encodeImagetoBase64(croppedImagePtah):
    with open(croppedImagePtah,"rb") as f:
        return base64.b64encode(f.read())