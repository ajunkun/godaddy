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


def align_feature_period(feature_df: pd.DataFrame, label_df: pd.DataFrame, period: int = 1) -> pd.DataFrame:
    """
    align period and feature dataframes for forecasting
    :param feature_df:
    :param label_df:
    :param period:
    :return:
    """

    pass
