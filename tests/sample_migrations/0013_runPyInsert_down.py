from infi.clickhouse_orm import migrations
from test_migrations import Model3

DELETE_QUERY = f"DELETE From `{Model3.table_name()}` Where date = '2016-01-04' "

operations = [
    migrations.RunSQL(DELETE_QUERY),
]
