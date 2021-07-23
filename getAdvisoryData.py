import requests
import tarfile

import io


def getAdvisoryData():
    print("geting advisory data")


    url = 'https://tgftp.nws.noaa.gov/SL.us008001/DF.sha/DC.cap/DS.WWA/current_all.tar.gz'

    print('Downloading shapefile...')
    
    target_path = 'current_all.tar.gz'

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            f.write(response.raw.read())

    tf = tarfile.open(target_path)
    tf.extractall()

    print("Done")




getAdvisoryData()
