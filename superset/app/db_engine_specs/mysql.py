import pandas as pd
from superset.db_engine_specs.mysql import MySQLEngineSpec as BaseSpec


class MySQLEngineSpec(BaseSpec):

    def __init__(self):
        super().__init__()

    @classmethod
    def df_to_sql(cls, df: pd.DataFrame, **kwargs):
        kwargs['method'] = 'multi'
        super().df_to_sql(df, **kwargs)
