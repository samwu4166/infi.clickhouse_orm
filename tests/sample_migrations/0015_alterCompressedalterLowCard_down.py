from infi.clickhouse_orm import migrations
from ..test_migrations import *

operations = [
    migrations.AlterTable(Model4),
    migrations.AlterTable(Model2)
]
