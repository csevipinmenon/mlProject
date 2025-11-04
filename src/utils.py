import numpy as np
import pandas as pd
import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logger
import dill


def save_object(file_path,obj):
    try:
        path_dir = os.path.dirname(file_path)
        os.makedirs(path_dir,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)