from src import logger
from src.pipeline.STAGE1_data_ingestion import DataIngestionPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
except Exception as e:
    logger.exception(e)
    raise e