from infi.clickhouse_orm import migrations

operations = [
    migrations.RunSQL("DELETE From `mig` Where date = '2016-01-01' "),
    migrations.RunSQL([
        "DELETE From `mig` Where date = '2016-01-02' ",
        "DELETE From `mig` Where date = '2016-01-03' ",
    ])
]
