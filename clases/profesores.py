from clases.personas import Persona

class Profesor(Persona):
    
    def __innit__(self):
        super().__init__()
        
        
    def leerDatosProfesor(self):
        self.clave = input("Clave: ")
        
    def mostrarDatosProfesor(self):
        print(self.clave)