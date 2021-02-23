import pandas as pd
import numpy as np

import automl_alex
from automl_alex import DataPrepare
from automl_alex import AutoML, AutoMLClassifier, AutoMLRegressor

MODEL_FILE_NAME = 'AutoML_model'
MODEL_DIR ='./model/'


def load_data():
    '''
    here you can insert your function to load data
    '''
    data = pd.read_csv('./data/openml_id_543_test.csv')
    return(data)


def send_predict(predict):
    '''
    here you can insert your function to send or save predicts
    '''
    np.savetxt("predict.csv", predict, delimiter=",")


def data_prepare(data):
    '''
    Here is a processing for raw data
    '''
    return(data)


def load_model(model_name, dir):
    model = AutoMLClassifier()
    model = model.load(model_name, dir=dir)
    return(model)


def model_predict():
    data = load_data()
    data = data_prepare(data)

    model = load_model(MODEL_FILE_NAME, MODEL_DIR)
    predict = model.predict(data)
    send_predict(predict)


if __name__ == '__main__':
    model_predict()