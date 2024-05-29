import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.config.configuration import ConfigurationManager
from src.components.callbacks import Callbacks
from src.components.model_training import Training
from src import logger

STAGE_NAME = 'Training'

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        callbacks_config = config.get_callbacks_config()
        callbacks = Callbacks(config=callbacks_config)
        callback_list = callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callbak_list=callback_list
        )

if __name__ == '__main__':
    try:
        logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
        training = ModelTrainingPipeline()
        training.main()
        logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
    except Exception as e:
        logger.exception(e)
        raise e