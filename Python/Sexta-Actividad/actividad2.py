class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print('Nombre: ',self.nombre)
        print('Nota: ',self.nota)

    def mensaje(self):
        if self.nota >= 5:
            print('APROBADO')
        else:
            print('DESAPROBADO')

alumnoAprobado = Alumno()
alumnoDesaprobado = Alumno()


alumnoAprobado.inicializar('Emiliano',8)
alumnoAprobado.imprimir()
alumnoAprobado.mensaje()
alumnoDesaprobado.inicializar('Daniel',4)
alumnoDesaprobado.imprimir()
alumnoDesaprobado.mensaje()








