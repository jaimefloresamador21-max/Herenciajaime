from clases.alumnos import Alumno
from clases.profesores import Profesor     


class Exalumno(Alumno,Profesor):
    def __innit__(self):
        super().__init__()
        self.titulo = ""
        
    def leerDatosExalumno(self):
        self.titulo =input("Título: ")
        
    def mostrarDatosExalumno(self):
        print(self.titulo)
        