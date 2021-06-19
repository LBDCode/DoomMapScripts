import io
import csv
import psycopg2
from decimal import Decimal
import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')


def parseTextFileAndWriteToDB():

    conn = psycopg2.connect(dbname=DB_NAME, port=PORT, user=USER,password=PASSWORD, host=HOST)

    cur = conn.cursor()

    with open('clean_data.txt', newline = '') as gage_data:
        gage_reader = csv.reader(gage_data, delimiter='\t')

        for gage in gage_reader:
            state_abv = gage[0]
            agency_cd = gage[1]
            site_no = gage[2]
            station_nm = gage[3]
            datum = float(gage[9]) if gage[9] != '' else 0
            latitude = Decimal(gage[5])
            longitude = Decimal(gage[6])
            active = True
            datum_type = gage[11]

            cur.execute('INSERT INTO gages(state_abv, agency_cd, site_no, station_nm, datum, location_geom, latitude, longitude, active, datum_type)'
    'VALUES (%(state_abv)s, %(agency_cd)s, %(site_no)s, %(station_nm)s, %(datum)s, ST_SetSRID(ST_MakePoint(%(x)s, %(y)s),4326), %(latitude)s, %(longitude)s, %(active)s, %(datum_type)s)',
    {'state_abv': state_abv, 'agency_cd': agency_cd, 'site_no': site_no, 'station_nm': station_nm, 'datum': datum, 'x': longitude, 'y': latitude, 'latitude': latitude, 'longitude': longitude, 'active': active, 'datum_type': datum_type})

    conn.commit()
    conn.close()




parseTextFileAndWriteToDB()