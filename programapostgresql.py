# -*- coding: utf-8 -*-

import psycopg2
import getpass
#definimos los parámetros para la conexión
usuario = raw_input('Nombre de usuario: ')
contras = getpass.getpass('Contraseña: ')
bd = raw_input('Nombre de la base de datos: ')
#hacemos una comprobación de usuario, contraseña y nombre de la base de datos
if usuario != 'cliente' or contras != 'cliente':
	print 'El usuario o la contraseña indicados no son correctos'
elif bd != 'base1':
	print 'La base de datos no existe'
else :
	conn = psycopg2.connect(database=bd, user=usuario, password=contras, host='10.1.1.51', port='5432') #le pasamos los parámetros para la conexión
	print 'Se ha establecido la conexión'
	cursor = conn.cursor()
	cursor.execute('select matricula, marca, color from coches') #hacemos la consulta
	lineas = cursor.fetchall() #leemos el resultado
	for linea in lineas: #mostramos las variables por pantalla con un bucle
		print 'Matrícula: '+linea[0]+', Marca: '+linea[1]+', Color: '+linea[2]
conn.close()
