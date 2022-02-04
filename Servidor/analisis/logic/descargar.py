import requests
import os
import sys
import datetime

from zipfile import ZipFile

sys.path.insert(0, os.path.dirname(__file__))


def descargar():
    file = 'datos_covid.zip'

    url = 'http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'
    r = requests.get(url, allow_redirects=True)

    open(file, 'wb').write(r.content)

    try:
        with ZipFile(file, 'r') as z:
            list_of_files = z.namelist()

            elem = list_of_files[0]
            
            z.extractall()

            os.rename(elem,'analisis/data/covid.csv')
            os.remove(file)
    except:
        return 'ERROR'
    return 'Archivo descargado exitosamente'
