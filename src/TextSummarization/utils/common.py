import os
from box.exceptions import BoxValueError
import yaml
from TextSummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ read yaml file and return
    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: If the yaml file is empty
        e: empty file
    
    Returns:
    ConfigBox: configBox type
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded yaml file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The yaml file at {path_to_yaml} is empty.")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if mutliple dirs is to be created. Defaults to False.
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of file

    Returns:
        strs: size in KB
    """
    size_in_kb = round(os.path.get_size(path) / 1024)
    return f"~ {size_in_kb} KB"