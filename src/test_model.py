"""Validate model performance"""

import argparse
import logging
import pandas as pd
from sklearn.metrics import mean_absolute_error
from joblib import load

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/test_model.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

VAL_DATA = 'data/proc/val.csv'
MODEL_PATH = 'models/random_forest.joblib'


def validate_model(model_path, data_path):
    df_val = pd.read_csv(data_path)
    x_val = df_val[['total_meters']]
    y_val = df_val['price']

    model = load(model_path)
    y_pred = model.predict(x_val)
    mae = mean_absolute_error(y_val, y_pred)

    r2 = model.score(x_val, y_val)
   # c = int(model.coef_[0])
    #inter = int(model.intercept_)

    logger.info(f'Validation completed: R2 = {r2:.3f}, MAE = {mae:.0f}')
    #logger.info(f'Predictive formula: Price = {c} * area + {inter}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model',
                        help='Path to the model file',
                        default=MODEL_PATH)
    parser.add_argument('-d', '--data',
                        help='Path to the validation data file',
                        default=VAL_DATA)
    args = parser.parse_args()
    validate_model(args.model, args.data)
