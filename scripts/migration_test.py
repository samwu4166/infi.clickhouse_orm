from infi.clickhouse_orm.database import Database, ServerError
from infi.clickhouse_orm.models import Model, BufferModel, Constraint, Index
from infi.clickhouse_orm.fields import *
from infi.clickhouse_orm.engines import *
from infi.clickhouse_orm.migrations import MigrationHistory

from enum import Enum
# Add tests to path so that migrations will be importable
import sys, os
sys.path.append(os.path.dirname(__file__))


import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logging.getLogger("requests").setLevel(logging.WARNING)


database = Database('test-db', log_statements=False)
database.migrate('tests.sample_migrations', 0)

# database.drop_table(MigrationHistory)
# database.drop_database()