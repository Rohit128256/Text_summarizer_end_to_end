import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations # This decorator is used to detect any datatype related error
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_obj:
            content = yaml.safe_load(yaml_obj)
            logging.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file doesn't exist")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories : list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose :
            logging.info(f"created directory with path : {path}")
                

@ensure_annotations
def get_size(path : Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"