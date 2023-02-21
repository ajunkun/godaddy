import pandas as pd


def combine_features(label_df: pd.DataFrame, feat_df: pd.DataFrame, n_period: int) -> pd.DataFrame:
    dataset = label_df.copy()
    for n in range(1, n_period):
        tmp_df = feat_df.copy()
        all_cols = list(tmp_df.columns)
        feat_cols = [col for col in all_cols if col not in ['cfips', 'year', 't']]
        chg_cols = [f'{col}_t_minus_{n}' for col in feat_cols]
        chg_dict = dict(zip(feat_cols, chg_cols))
        tmp_df = tmp_df.rename(columns=chg_dict)
        dataset = dataset.merge(tmp_df, left_on=[f't_minus_{n}', 'cfips'], right_on=['t', 'cfips'], how='left')

    # TODO: add join period t-n features
    return dataset


def get_t_minus_n_period(df: pd.DataFrame, column_nm: str, n_period: int) -> pd.DataFrame:
    for i in range(1, n_period+1):
        df[f'{column_nm}_minus_{i}'] = df[column_nm] - pd.DateOffset(months=i)

    return df


def populate_period(feature_df: pd.DataFrame, col_nm: str, freq_tp: str) -> pd.DataFrame:
    if freq_tp == 'yearly':
        month_df = pd.DataFrame({'month': [f'{str(i).zfill(2)}-01' for i in range(1, 13)]})

        # cross join
        feature_df['tmp_key'] = 0
        month_df['tmp_key'] = 0
        feature_df = feature_df.merge(month_df, on='tmp_key', how='outer')
        feature_df = feature_df.drop(columns='tmp_key')
    feature_df['t'] = feature_df['year'] + '-' + feature_df['month']
    feature_df['t'] = pd.to_datetime(feature_df['t'])
    feature_df.drop(columns='month', inplace=True)

    return feature_df
