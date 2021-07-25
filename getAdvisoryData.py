import requests
import tarfile
import io
import os
import subprocess
import psycopg2
from dotenv import load_dotenv



def getAdvisoryData():
    print("geting advisory data")


    url = 'https://tgftp.nws.noaa.gov/SL.us008001/DF.sha/DC.cap/DS.WWA/current_all.tar.gz'

  
    target_path = 'advisoryData/current_all.tar.gz'

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            f.write(response.raw.read())

    tf = tarfile.open(target_path)
    tf.extractall('./advisoryData')



def updateDatabase():
    
    load_dotenv()

    DB_NAME = os.getenv('DB_NAME')
    PORT = os.getenv('PORT')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    AREA_TABLE=os.getenv('AREA_TABLE')


    conn = psycopg2.connect(dbname=DB_NAME, port=PORT, user=USER,password=PASSWORD, host=HOST)
    cur = conn.cursor()

    cur.execute("DELETE FROM {0}".format(AREA_TABLE))

    conn.commit()
    conn.close()
    

    cmd = 'shp2pgsql -a ./advisoryData/current_all.shp public.{0} | psql -q -h localhost -d {1} -U {2}'.format(AREA_TABLE, DB_NAME, USER)

    subprocess.call(cmd, shell=True)


getAdvisoryData()
updateDatabase()