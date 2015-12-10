# -*- coding: utf-8 -*-

import cx_Oracle
import getpass

#definimos los parámetros necesarios
usuario = raw_input('Nombre de usuario: ')
contras = getpass.getpass('Contraseña: ')
SID = raw_input('SID de la base de datos: ')

conn = cx_Oracle.connect(usuario+'/'+contras+'@192.168.1.195/'+SID) #establecemos la conexión con los parámetros recibidos
cursor = conn.cursor() #creamos un cursor
cursor.execute('select ENAME, DNAME from EMP, DEPT where EMP.DEPTNO = DEPT.DEPTNO') #realizamos la consulta
for result in cursor: #leemos el resultado
        print result #mostramos el resultado por pantalla
cursor.close()
conn.close()
