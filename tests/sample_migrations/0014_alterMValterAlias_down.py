from infi.clickhouse_orm import migrations
from ..test_migrations import *

operations = [
    migrations.AlterTable(MaterializedModel),
    migrations.AlterTable(AliasModel)
]
