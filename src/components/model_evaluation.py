import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import custom_exception
import os
import sys 
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from urllib.parse import urlparse 
import mlflow 
import mlflow.sklearn 
import pickle 
from src.utils.utils import load_object

@dataclass
class ModelEvaluationConfig:
    pass 

class ModelEvaluation:
    def __init__(self):
        pass 

    def initiate_model_evaluation(self):
        try:
            pass

        except Exception as e:
            logging.info()
            raise custom_exception(e, sys)
    