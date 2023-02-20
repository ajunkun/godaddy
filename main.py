import os
import pandas as pd

from configs import TRAIN_PATH, CENSUS_STARTER_PATH, OUTPUT_PATH, TEST_PATH, n_period
from helper_functions import get_t_minus_n_period
from feature.census_starter import get_census_starter_feats


pd.set_option('display.max_columns', 20)
train_df = pd.read_csv(TRAIN_PATH, parse_dates=['first_day_of_month'])
census_df = get_census_starter_feats()
test_df = pd.read_csv(TEST_PATH)

train_df.rename(columns={'first_day_of_month': 't'}, inplace=True)
train_df = get_t_minus_n_period(df=train_df, column_nm='t', n_period=n_period)

print(census_df.head())
