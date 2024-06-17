"""Train model and save checkpoint"""
import argparse
import logging
import pandas as pd
from joblib import dump
from catboost import CatBoostRegressor
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/train_model.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

TRAIN_DATA = 'data/proc/train.csv'
MODEL_SAVE_PATH = 'models/catboost.joblib'


def train_model(train_data_path, model_save_path):
    df_train = pd.read_csv(train_data_path)
    X_train = df_train[['rooms_count', 'author_type', 'floor', 'street',
       'underground', 'floors_count', 'district', 'total_meters']]
    y_train = df_train['price']

    cat_features = ['author_type', 'district', 'street', 'underground']
    model = CatBoostRegressor(cat_features=cat_features)
    model.fit(X_train, y_train)
    dump(model, model_save_path)

    r2 = model.score(X_train, y_train)
    #c = int(linear_model.coef_[0])
    #inter = int(linear_model.intercept_)

    logger.info(f'Model trained and saved to {model_save_path}')
    logger.info(f'Training R2 = {r2:.3f}')
    #logger.info(f'Training formula: Price = {c} * area + {inter}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model',
                        help='Model save path',
                        default=MODEL_SAVE_PATH)
    parser.add_argument('-t', '--train_data',
                        help='Path to the train data file',
                        default=TRAIN_DATA)
    args = parser.parse_args()
    train_model(args.train_data, args.model)
