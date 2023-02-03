import pandas as pd


def combine_features(train_df: pd.DataFrame, feat_df: pd.DataFrame) -> pd.DataFrame:
    """
    :param train_df: dataframe with row_id and label
    :param feat_df: dataframe witr features and row_id
    :return:
    """
    combined_df = train_df.merge(feat_df, on='row_id', how='left')
    return combined_df
