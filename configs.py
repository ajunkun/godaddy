import os


DIR_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(DIR_PATH, "data")

TRAIN_PATH = os.path.join(DATA_PATH, "train.csv")
TEST_PATH = os.path.join(DATA_PATH, "test.csv")

CENSUS_STARTER_PATH = os.path.join(DATA_PATH, "census_starter.csv")
REVEALED_TEST_PATH = os.path.join(DATA_PATH, "revealed_test.csv")
SAMPLE_SUBMISSION_PATH = os.path.join(DATA_PATH, "sample_submission.csv")

CENSUS_2020_PATH = os.path.join(DATA_PATH, "ACSST5Y2020.S0101-Data.csv")
CENSUS_2021_PATH = os.path.join(DATA_PATH, "ACSST5Y2021.S0101-Data.csv")

OUTPUT_PATH = os.path.join(DIR_PATH, "output")
