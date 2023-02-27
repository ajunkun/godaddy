import os
import pandas as pd

from configs import TRAIN_PATH, CENSUS_STARTER_PATH, OUTPUT_PATH, TEST_PATH, n_period
from helper_functions import get_timestep, get_md_series, convert_feats_to_series
from feature.census_starter import cln_census_starter_df


pd.set_option('display.max_columns', 20)
train_df = pd.read_csv(TRAIN_PATH, parse_dates=['first_day_of_month'])
census_df = pd.read_csv(CENSUS_STARTER_PATH)
test_df = pd.read_csv(TEST_PATH)

# label
time_step_df = get_timestep(train_df=train_df)
mb_series = get_md_series(train_df=train_df)

# feature
census_df = cln_census_starter_df(census_df=census_df)
features = time_step_df.merge(census_df, on=['year', 'cfips'], how='left')
features = convert_feats_to_series(feature_df=features)
