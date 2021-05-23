import requests
from zipfile import ZipFile
import pandas as pd
import numpy as np
import MySQLdb

file = 'datos_covid.zip'

url = 'http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'
r = requests.get(url, allow_redirects=True)

open(file, 'wb').write(r.content)

try:
    with ZipFile(file, 'r') as z:
        list_of_files = z.namelist()

        for elem in list_of_files:
            print(elem)
        
        z.extractall()
        print('archivos extraidos')
except:
    print('ERROR')
print(elem)
