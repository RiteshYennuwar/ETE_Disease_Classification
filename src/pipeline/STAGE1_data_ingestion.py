import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f'---->> Stage {STAGE_NAME} Started <<----')
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f'---->> Stage {STAGE_NAME} Completed <<----\n\nx===================x')
    except Exception as e:
        logger.exception(e)
        raise e