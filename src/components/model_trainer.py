import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import custom_exception
import os
import sys 
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 
from pathlib import Path
from src.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, Ridge, Lasso 

@dataclass
class ModelTrainerConfig:
    pass 

class ModelTrainer:
    def __init__(self):
        pass 

    def initiate_model_training(self):
        try:
            pass 

        except Exception as e:
            logging.info()
            raise custom_exception(e, sys)
    