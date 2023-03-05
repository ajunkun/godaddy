import pandas as pd
import numpy as np


def smape_comp(y_true, y_pred):
    """
    Calculate Symmetric Mean Absolute Percentage Error (SMAPE)
    """
    mask = (y_true != 0) | (y_pred != 0)
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
    numerator = np.abs(y_true - y_pred)
    smape_val = np.where(mask, numerator / denominator, 0)
    return np.mean(smape_val) * 100
