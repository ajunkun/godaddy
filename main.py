import os

import numpy as np
import pandas as pd
import darts
from darts.models import NBEATSModel
from pytorch_lightning.callbacks import EarlyStopping
from torchmetrics import MeanSquaredError
from torchmetrics import SymmetricMeanAbsolutePercentageError

from configs import TRAIN_PATH, CENSUS_STARTER_PATH, OUTPUT_PATH, TEST_PATH, lookback_steps, predict_steps, train_size
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

# train/val split
cut_pt = int(np.floor(len(mb_series) * train_size))
mb_train, mb_val = mb_series[:cut_pt], mb_series[cut_pt:]
features_train, features_val = features[:cut_pt], features[cut_pt:]

# model
metrics = MeanSquaredError()
# my_stopper = EarlyStopping(monitor="val_MeanAbsolutePercentageError", patience=5, min_delta=0.05, mode='min')
pl_settings = {'accelerator': 'gpu', 'devices': -1,
               # "callbacks": [my_stopper]
               }

model = NBEATSModel(input_chunk_length=lookback_steps, output_chunk_length=predict_steps,
                    n_epochs=500, pl_trainer_kwargs=pl_settings, torch_metrics=metrics)
model.fit(series=mb_train, val_series=mb_val, past_covariates=features_train, val_past_covariates=features_val,
          verbose=False)
