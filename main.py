from src.textSummarizer.logging import logging
from src.textSummarizer.pipeline.s1_data_ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.s2_data_validation import DataValidationPipeline
from box.exceptions import BoxValueError

STAGE_NAME = "Data Validation Stage"

try:
    logging.info(f">>>>> stage{STAGE_NAME} started")
    data_ingestion_obj = DataValidationPipeline()
    data_ingestion_obj.main()
    logging.info(f">>>>> stage{STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in data validation")
except Exception as e:
    raise e
