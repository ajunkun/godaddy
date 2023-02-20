import pandas as pd


def combine_features(train_df: pd.DataFrame, feat_df: pd.DataFrame) -> pd.DataFrame:
    """
    :param train_df: dataframe with row_id and label
    :param feat_df: dataframe witr features and row_id
    :return:
    """
    combined_df = train_df.merge(feat_df, on='row_id', how='left')
    return combined_df


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

    return feature_df
