from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_training import ModelTrainer
from src.textSummarizer.logging import logging

# Entity -> Manager -> Component -> integration_to_pipeline -> 

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()