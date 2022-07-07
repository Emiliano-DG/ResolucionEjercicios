import sqlite3

coneccion = sqlite3.connect('fichero.db')
cursor = coneccion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE alumnos ( id INT , Nombre VARCHAR(80),Apellido VARCHAR(80))")

#Insertar alumnos
cursor.execute("INSERT INTO alumnos VALUES(1,'Lionel', 'Messi')")
cursor.execute("INSERT INTO alumnos VALUES(2,'Leandro', 'Paredes')")
cursor.execute("INSERT INTO alumnos VALUES(3,'Rodrigo', 'Depaul')")
cursor.execute("INSERT INTO alumnos VALUES(4,'Emiliano', 'Martinez')")
cursor.execute("INSERT INTO alumnos VALUES(5,'Pepe', 'Rodriguez')")
cursor.execute("INSERT INTO alumnos VALUES(6,'Pepito', 'Gonzalez')")
cursor.execute("INSERT INTO alumnos VALUES(7,'Eduardo', 'Tatengue')")
cursor.execute("INSERT INTO alumnos VALUES(8,'Jorge', 'Nadie')")

coneccion.commit()

#Mostrar datos de un alumno
cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Pepe'")
mostrar = cursor.fetchall()
print(mostrar)
coneccion.close()