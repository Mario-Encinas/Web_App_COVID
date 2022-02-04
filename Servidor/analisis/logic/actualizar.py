import requests
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(__file__))


def actualizar():
    ahora = datetime.datetime.utcnow()
    tres_meses = ahora - datetime.timedelta(days=120)

    #calculando numero de registros
    lengt = 0
    with open('covid.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            lengt += 1


    #estableciendo conección a la base de datos.
    username = 'siyciseo_app_covid'
    password = '2}flEBZS)Ccp'
    hostname = 'localhost'
    database = 'siyciseo_app_covid'

    try: 
    	myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    	cur = myConnection.cursor()
    except Exception as e: 
    	myConnection.close()
    	exit()


    Informacion_paciente = pd.DataFrame()
    Antecedentes_paciente = pd.DataFrame()
    Datos_medicos = pd.DataFrame()

    #copiando datos desde archvio csv a base de datos
    for i in range(1, (lengt+1), 10000):

    	df = pd.read_csv("analisis/data/covid.csv'", skiprows = i, nrows=(10000), header=None)
    	columnas = df.columns

    	df[columnas[12]] = df[columnas[12]].replace(['9999-99-99'], '2099-12-12')

    	df[columnas[10]] = pd.to_datetime(df[columnas[10]])
	    df[columnas[11]] = pd.to_datetime(df[columnas[11]])
    	df[columnas[12]] = pd.to_datetime(df[columnas[12]])

    	df = df.loc[(df[columnas[11]] > tres_meses)]

    	columnas_paciente = [1,5,7,8,9,10,11,12,13,15,30,39,35]
	    columnas_antecedentes = [1,14,17,20,21,22,23,24,25,26,27,28,29]
    	columnas_datos_medicos = [1,2,3,4,31,32,33,34]

    	Informacion_paciente = df[columnas[columnas_paciente]]
    	Antecedentes_paciente = df[columnas[columnas_antecedentes]]
    	Datos_medicos = df[columnas[columnas_datos_medicos]]
    
    	paciente = Informacion_paciente.values.tolist()
    	llaves = Informacion_paciente[1].values.tolist()
    	antecedentes = Antecedentes_paciente.values.tolist()
    	medico = Datos_medicos.values.tolist()
    
    	try:

    		cur.executemany("""DELETE FROM analisis_datos_pacientes
						    WHERE ID = (%s)""",llaves)
    		cur.executemany("""DELETE FROM analisis_antecedentes_pacientes
    						WHERE ID = (%s)""",llaves)
    		cur.executemany("""DELETE FROM analisis_informacion_medica
    						WHERE ID = (%s)""",llaves)

    		cur.executemany("""INSERT INTO analisis_datos_pacientes
                            (ID,sexo,entidad,municipio,tipo,fecha_ingrezo,fecha_sintomas,
                            fecha_defuncion,intubado,edad,contacto_otro_caso,uci,clasificacion_final)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", paciente)
    
    		cur.executemany("""INSERT INTO analisis_antecedentes_pacientes
                            (ID,neumonia,embarazo,diabetes,epoc,asma,inmunosuprimido,
                            hipertencion,otra_complicacion,enfermedad_cardiovascular,
                            obesidad,insuficiencia_renal_cronica,tabaquismo)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", antecedentes)

		    cur.executemany("""INSERT INTO analisis_informacion_medica
                          (ID,origen,sector,entidad_unidad_medica,toma_muestra_laboratorio,
                          resultado_laboratorio,toma_muestra_antigeno,resultado_antigeno)
                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", medico)

    	except Exception as e: 
    		myConnection.close()
    		print("Error: ",e)
    		exit()


    myConnection.close()
    return 'Datos actualizados'
