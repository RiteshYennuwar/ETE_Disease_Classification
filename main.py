from src import logger
from src.pipeline.STAGE1_data_ingestion import DataIngestionPipeline
from src.pipeline.STAGE2_base_model import BaseModelPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Base Model'

try:
    logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
    base_model = BaseModelPipeline()
    base_model.main()
    logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
except Exception as e:
    logger.exception(e)
    raise e