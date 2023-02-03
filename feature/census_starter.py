import pandas as pd
from configs import CENSUS_STARTER_PATH


def get_census_starter_feats() -> pd.DataFrame:
    census_df = pd.read_csv(CENSUS_STARTER_PATH)
    all_cols = list(census_df.columns)
    feature_cols = [col for col in all_cols if col != 'cfips']
    feature_nms = list(set([col[:-5] for col in feature_cols]))

    tmp_df = pd.melt(census_df, id_vars='cfips', value_vars=feature_cols, var_name='feature')
    tmp_df.loc[:, 'year'] = tmp_df['feature'].str[-4:]
    tmp_df.loc[:, 'feature'] = tmp_df['feature'].str[:-5]
    census_features = pd.pivot_table(tmp_df, index=['cfips', 'year'], columns='feature', values='value').reset_index()

    # populate 12 months
    month_df = pd.DataFrame({'month': [f'{str(i).zfill(2)}-01' for i in range(1, 13)]})

    # cross join
    census_features['tmp_key'] = 0
    month_df['tmp_key'] = 0

    census_features = census_features.merge(month_df, on='tmp_key', how='outer')
    census_features = census_features.drop(columns='tmp_key')
    census_features['row_id'] = census_features['cfips'].astype(str) + '_' + \
                                census_features['year'] + '-' + census_features['month']
    census_features = census_features[['row_id'] + feature_nms]
    return census_features
