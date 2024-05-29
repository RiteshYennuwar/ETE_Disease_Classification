import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.config.configuration import ConfigurationManager
from src.components.base_model import BaseModel
from src import logger

STAGE_NAME = 'Base Model'

class BaseModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.updated_base_model()

if __name__ == '__main__':
    try:
        logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
        base_model = BaseModelPipeline()
        base_model.main()
        logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
    except Exception as e:
        logger.exception(e)
        raise e