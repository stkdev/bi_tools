import superset
from superset.db_engine_specs import engines

from .db_engine_specs.mysql import MySQLEngineSpec

app = superset.app

engines[MySQLEngineSpec.engine] = MySQLEngineSpec
