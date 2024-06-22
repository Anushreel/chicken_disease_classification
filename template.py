import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

project_name="chicken_disease_classification"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    "templates/index.html"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath) # returns folder and file name
    if filedir !="": #not empty
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # is path present or if the file of file is zero that is no content
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"file already exist : {filepath}")


