
import requests
import io
import io
import csv
import psycopg2
from decimal import Decimal
import os
import json
from dotenv import load_dotenv

load_dotenv()


def getAdvisoryData():
    print("geting advisory data")


    DB_NAME = os.getenv('DB_NAME')
    PORT = os.getenv('PORT')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')

    # conn = psycopg2.connect(dbname=DB_NAME, port=PORT, user=USER,password=PASSWORD, host=HOST)

    # cur = conn.cursor()

    url = "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/Current_WildlandFire_Locations/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json" 
    response = requests.get(url).json()
    fires = response['features']

    for fire in fires:
         geom = fire["geometry"]
         type = geom['type'] if geom else None
         coordinates = geom['coordinates'] if geom else None

         data = {
             "type": type,
            "coordinates": coordinates
        }



         effective = advisory["properties"]["effective"]
        #  cur.execute('INSERT INTO weather_advisory_areas (effective, onset, expires, ends, status, severity, certainty, event_type, headline, description, instruction, area_description, ugc_geocode)'
        #     'VALUES (%(effective)s, %(onset)s, %(expires)s, %(ends)s, %(status)s, %(severity)s, %(certainty)s, %(event_type)s, %(headline)s, %(description)s, %(instruction)s, %(area_description)s, %(geocode)s)',
        #     {'effective': effective, 'onset': onset, 'expires': expires, 'ends': ends, 'status': status, 'severity': severity, 'certainty': certainty, 'event_type': event, 'headline': headline, 'description': description, 'instruction': instruction, 'area_description': area_description, 'geocode': geocode})



    conn.commit()
    conn.close()

getAdvisoryData()
