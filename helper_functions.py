import pandas as pd
import darts


def get_timestep(train_df: pd.DataFrame) -> pd.DataFrame:
    time_idx = train_df[['first_day_of_month', 'cfips']].drop_duplicates()
    time_idx.columns = ['time_step', 'cfips']
    time_idx['year'] = time_idx['time_step'].dt.year
    time_idx['month'] = time_idx['time_step'].dt.month
    time_idx['day'] = time_idx['time_step'].dt.day
    return time_idx


def get_md_series(train_df):
    series = train_df[['first_day_of_month', 'cfips', 'microbusiness_density']]
    series = darts.TimeSeries.from_group_dataframe(series, group_cols='cfips', time_col='first_day_of_month',
                                                   value_cols='microbusiness_density')
    return series


def convert_feats_to_series(feature_df: pd.DataFrame) -> darts.TimeSeries:
    feature_cols = [col for col in list(feature_df.columns) if col not in ['time_step', 'cfips',
                                                                           'year', 'month', 'day']]
    feat_series = darts.TimeSeries.from_group_dataframe(feature_df, group_cols='cfips', time_col='time_step',
                                                        value_cols=feature_cols)
    return feat_series
