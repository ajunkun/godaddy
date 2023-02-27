import pandas as pd
from configs import CENSUS_STARTER_PATH


def cln_census_starter_df(census_df: pd.DataFrame) -> pd.DataFrame:
    all_cols = list(census_df.columns)
    feature_cols = [col for col in all_cols if col != 'cfips']
    feature_nms = list(set([col[:-5] for col in feature_cols]))

    tmp_df = pd.melt(census_df, id_vars='cfips', value_vars=feature_cols, var_name='feature')
    tmp_df.loc[:, 'year'] = tmp_df['feature'].str[-4:].astype(int)
    tmp_df.loc[:, 'feature'] = tmp_df['feature'].str[:-5]
    census_features = pd.pivot_table(tmp_df, index=['cfips', 'year'], columns='feature', values='value').reset_index()
    return census_features
