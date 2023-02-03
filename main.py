import os
import pandas as pd

from configs import TRAIN_PATH, CENSUS_STARTER_PATH, OUTPUT_PATH
from helper_functions import combine_features
from feature.census_starter import get_census_starter_feats

train_df = pd.read_csv(TRAIN_PATH)
census_df = get_census_starter_feats()

train_df = combine_features(train_df, census_df)
