from peewee import *

pg_db = PostgresqlDatabase(
    'tourist2',
    user='Avtandil',
    password='12345',
    host='localhost',
    port=5432
)

class InnerFlights(Model):
    id = PrimaryKeyField(unique=True)
    from_region = CharField()
    to_destination = CharField()
    company = CharField()
    quantity = IntegerField()

    class Meta:
        database = pg_db
        order_by = 'id'
        db_table = 'inner_flights'


class OutterFlights(Model):
    id = PrimaryKeyField(unique=True)
    from_country = CharField()
    to_country = CharField()
    flight_type = CharField()
    company = CharField()
    neighbors = IntegerField()

    class Meta:
        database = pg_db
        order_by = 'id'
        db_table = 'outter_flights'