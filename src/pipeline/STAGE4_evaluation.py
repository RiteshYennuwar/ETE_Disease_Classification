import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.config.configuration import ConfigurationManager
from src.components.evaluation import Evaluation
from src import logger

STAGE_NAME = 'Evaluation'

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_validation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
        evaluation = EvaluationPipeline()
        evaluation.main()
        logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
    except Exception as e:
        logger.exception(e)
        raise e
         