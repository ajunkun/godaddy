import os


DIR_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(DIR_PATH, 'data')

TRAIN_PATH = os.path.join(DATA_PATH, 'train.csv')
TEST_PATH = os.path.join(DATA_PATH, 'test.csv')

CENSUS_STARTER_PATH = os.path.join(DATA_PATH, 'census_starter.csv')

OUTPUT_PATH = os.path.join(DIR_PATH, 'output')

lookback_steps = 12
predict_steps = 6

train_size = 0.8
