import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logging
from src.textSummarizer.utils.common import get_size
from pathlib import Path
from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )

            logging.info(f"{filename} downloading! with following info: \n{headers}")
        else:
            logging.info(f"The file already exists of size : {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_obj:
            zip_obj.extractall(unzip_path)

