from infi.clickhouse_orm import migrations
from ..test_migrations import *

operations = [
    migrations.DropTable(Model4Buffer),
    migrations.DropTable(Model4)
]
