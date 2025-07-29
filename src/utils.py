import os
import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save an object to a file using numpy's save function.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        print(f"Error saving object: {e}")
        raise CustomException(e, sys) from e
    
def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    """
    Evaluate the performance of different regression models.
    Returns a dictionary with model names as keys and their evaluation metrics as values.
    """
    try:
        report = {}
        for i in range (len(list(models))):
            model = list(models.values())[i]
            p = params[list(models.keys())[i]]

            grid_search = GridSearchCV(model, p, cv=3)
            # model.fit(X_train, y_train)
            grid_search.fit(X_train, y_train)

            model.set_params(**grid_search.best_params_)
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)
            y_train_pred = model.predict(X_train)

            train_model_r2_score = r2_score(y_train, y_train_pred)
            test_model_r2_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_r2_score

            return report
    except Exception as e:
        raise CustomException(e, sys)