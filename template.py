import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'Disease_classification(CNN)'

lsit_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/utils/__init__.py',
    'src/config/__init__.py',
    'src/config/configuration.py',
    'src/pipeline/__init__.py',
    'src/entity/__init__.py',
    'src/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb'
]

for filepath in lsit_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating:{filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filepath}')
    else:
        logging.info(f'{filepath} already exists')