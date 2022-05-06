from ast import In
from models import *
import psycopg2

data_inner_flight = [
{'from_region': 'Dagestan', 'to_destination': 'Kazahstan', 'company': 'Pegasus', 'quantity': 123},
{'from_region': 'Almaty', 'to_destination': 'Talas', 'company': 'Universal', 'quantity': 50},
{'from_region': 'Osh', 'to_destination': 'Kazahstan', 'company': 'Alma', 'quantity': 200},
{'from_region': 'Piter', 'to_destination': 'Moscow', 'company': 'Fly-Moscow', 'quantity': 100},
{'from_region': 'Dagestan', 'to_destination': 'Bishkek', 'company': 'Unknown', 'quantity': 123},
{'from_region': 'Bishkek', 'to_destination': 'Almaty', 'company': 'Pegasus', 'quantity': 57},
{'from_region': 'Dagestan', 'to_destination': 'Chui', 'company': 'Unknown', 'quantity': 200},
{'from_region': 'Dagestan', 'to_destination': 'Kazahstan', 'company': 'Pegasus', 'quantity': 300},
{'from_region': 'Chui', 'to_destination': 'Osh', 'company': 'Pegasus', 'quantity': 50},
{'from_region': 'Dagestan', 'to_destination': 'Kazahstan', 'company': 'Pegasus', 'quantity': 123},
{'from_region': 'Taras', 'to_destination': 'Tokmok', 'company': 'Unknown', 'quantity': 123},
{'from_region': 'Bishkek', 'to_destination': 'Bishkek', 'company': 'Pegasus', 'quantity': 90},
{'from_region': 'Stambul', 'to_destination': 'Kazahstan', 'company': 'Unknown', 'quantity': 100},
{'from_region': 'Dagestan', 'to_destination': 'Sochi', 'company': 'Pegasus', 'quantity': 123},
{'from_region': 'Naryn', 'to_destination': 'Batken', 'company': 'Pegasus', 'quantity': 24}]

data_outter_flight = [
{'from_country': 'Russia', 'to_country': 'Kazahstan', 'flight_type': 'Пассажирский', 'company': 'Pegasus', 'neighbors': 10},
{'from_country': 'Kyrgyzstan', 'to_country': 'Kazahstan', 'flight_type': 'Грузовой', 'company': 'Universal', 'neighbors': 0},
{'from_country': 'Turkie', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 4},
{'from_country': 'China', 'to_country': 'Polish', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 7},
{'from_country': 'Russia', 'to_country': 'Germany', 'flight_type': 'Грузовой', 'company': 'Alma', 'neighbors': 20},
{'from_country': 'Japan', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 1},
{'from_country': 'Turkie', 'to_country': 'Egypt', 'flight_type': 'Грузовой', 'company': 'Alma', 'neighbors': 6},
{'from_country': 'Kyrgyzstan', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 67},
{'from_country': 'Turkie', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 9},
{'from_country': 'Uzbekistan', 'to_country': 'Uzbekstan', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 10},
{'from_country': 'Turkie', 'to_country': 'Korea', 'flight_type': 'Грузовой', 'company': 'Alma', 'neighbors': 9},
{'from_country': 'Uzbekistan', 'to_country': 'Uzbekstan', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 10},
{'from_country': 'China', 'to_country': 'China', 'flight_type': 'Грузовой', 'company': 'Alma', 'neighbors': 9},
{'from_country': 'Uzbekistan', 'to_country': 'Uzbekstan', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 2},
{'from_country': 'Turkie', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 9},
{'from_country': 'Kyrgyzstan', 'to_country': 'Russia', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 10},
{'from_country': 'Turkie', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 90},
{'from_country': 'Uzbekistan', 'to_country': 'Uzbekstan', 'flight_type': 'Грузовой', 'company': 'Alma', 'neighbors': 4},
{'from_country': 'Turkie', 'to_country': 'China', 'flight_type': 'Пассажирский', 'company': 'Alma', 'neighbors': 9},
{'from_country': 'Kyrgyzstan', 'to_country': 'Uzbekstan', 'flight_type': 'Грузовой', 'company': 'Alma', 'neighbors': 7}]

with pg_db:
    pg_db.create_tables([InnerFlights, OutterFlights])

    # 1
    #InnerFlights.insert_many(data_inner_flight).execute()
    #OutterFlights.insert_many(data_outter_flight).execute()

    # 2
    # for i in InnerFlights.select():
    #     print(i.id, i.from_region, i.to_destination, i.company, i.quantity)

    # 3
    # query = InnerFlights.select().where(InnerFlights.id > 10)
    # for i in query:
    #     print(i.id, i.from_region, i.to_destination, i.company, i.quantity)

    # 4
    # query = InnerFlights.select().where((InnerFlights.to_destination == 'Osh') | (InnerFlights.to_destination == 'Bishkek'))
    # for i in query:
    #     print(i.id, i.from_region, i.to_destination, i.company, i.quantity)

    # 5
    # query = InnerFlights.select().where(InnerFlights.quantity > 150)
    # for i in query:
    #     print(i.id, i.from_region, i.to_destination, i.company, i.quantity)

    # 6
    # query = OutterFlights.select().where(OutterFlights.flight_type == 'Пассажирский')
    # for i in query:
    #     print(i.company)

    # 7
    # query = OutterFlights.select().where(OutterFlights.id < 7)
    # for i in query:
    #     print(i.id, i.from_country, i.to_country, i.flight_type, i.company, i.neighbors)

    # 8
    # query = OutterFlights.select().where(OutterFlights.flight_type == 'Грузовой')
    # for i in query:
    #     print(i.id, i.from_country, i.to_country, i.flight_type, i.company, i.neighbors)

    # 9
    # query = OutterFlights.select().where(OutterFlights.neighbors < 3)
    # for i in query:
    #     print(i.id, i.from_country, i.to_country, i.flight_type, i.company, i.neighbors)

    # 10
    # query = OutterFlights.select().where((OutterFlights.neighbors < 3) & (OutterFlights.flight_type == 'Пассажирский'))
    # for i in query:
    #     print(i.id, i.from_country, i.to_country, i.flight_type, i.company, i.neighbors)

    # 11
    # query = OutterFlights.select()
    # for i in query:
    #     print(i.company,  i.from_country)

