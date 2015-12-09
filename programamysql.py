# -*- coding: utf-8 -*-
import MySQLdb
import getpass

usuario = raw_input('Nombre de usuario: ')
contras = getpass.getpass('Contraseña: ') #utilizamos getpass para ocultar la contraseña
bd = raw_input('Nombre de la base de datos: ')

if usuario != 'cliente' or contras != 'cliente':
	print 'El usuario o la contraseña indicados no son correctos'
elif bd != 'base1':
	print 'La base de datos no existe'
else :
	conn = MySQLdb.connect('10.1.1.51',usuario,contras,bd)
	print conn #verificamos que se establece la conexión
	cursor = conn.cursor()
	cursor.execute('select matricula, marca, color from coches') #hacemos una consulta sencilla
	for a in range(cursor.rowcount):
		resultado = cursor.fetchone() #obtenemos el resultado
		print 'Matrícula: '+resultado[0]+', Marca: '+resultado[1]+', Color: '+resultado[2] #mostramos el resultado por pantalla
	conn.close() #cerramos la conexión
