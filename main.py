from src.textSummarizer.logging import logging
from src.textSummarizer.pipeline.s1_data_ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.s2_data_validation import DataValidationPipeline
from src.textSummarizer.pipeline.s3_data_transformation import DataTransformationPipeline
from src.textSummarizer.pipeline.s4_model_trainer import ModelTrainerPipeline
from src.textSummarizer.pipeline.s5_model_evaluation import ModelEvaluationPipeline
from box.exceptions import BoxValueError

# Entity(config_template) -> configuration_manager(gives_config_obj by using config_template from entity) -> components(takes the config_object and does the work according to its tasks) --(integration with pipeline)-> Pipeline(using configuration_manager and components we will define a pipeline or series of steps for the work to be done)

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>> stage - {STAGE_NAME} started")
    data_ingestion_obj = DataIngestionPipeline()
    data_ingestion_obj.main()
    logging.info(f">>>>> stage - {STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in Data Ingestion")
except Exception as e:
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logging.info(f">>>>> stage - {STAGE_NAME} started")
    data_validation_obj = DataValidationPipeline()
    data_validation_obj.main()
    logging.info(f">>>>> stage - {STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in Data Validation")
except Exception as e:
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logging.info(f">>>>> stage - {STAGE_NAME} started")
    data_trans_obj = DataTransformationPipeline()
    data_trans_obj.main()
    logging.info(f">>>>> stage - {STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in Data Transformation")
except Exception as e:
    raise e


STAGE_NAME = "Model Training"

try:
    logging.info(f">>>>> stage - {STAGE_NAME} started")
    model_tariner_obj = ModelTrainerPipeline()
    model_tariner_obj.main()
    logging.info(f">>>>> stage - {STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in Model Training")
except Exception as e:
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logging.info(f">>>>> stage - {STAGE_NAME} started")
    model_evaluation_obj = ModelEvaluationPipeline()
    model_evaluation_obj.main()
    logging.info(f">>>>> stage - {STAGE_NAME} completed")

except BoxValueError as e:
    raise ValueError("problem happened in Model Evaluation")
except Exception as e:
    raise e
