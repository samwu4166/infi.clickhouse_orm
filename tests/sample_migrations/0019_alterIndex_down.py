from infi.clickhouse_orm import migrations
from ..test_migrations import *

operations = [
    migrations.AlterIndexes(ModelWithIndex, reindex=True)
]
