from src.textSummarizer.logging import logging
from src.textSummarizer.pipeline.s1_data_ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.s2_data_validation import DataValidationPipeline
from src.textSummarizer.pipeline.s3_data_transformation import DataTransformationPipeline
from box.exceptions import BoxValueError

STAGE_NAME = "Data Transformation Stage"

try:
    logging.info(f">>>>> stage{STAGE_NAME} started")
    data_trans_obj = DataTransformationPipeline()
    data_trans_obj.main()
    logging.info(f">>>>> stage{STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in data validation")
except Exception as e:
    raise e
