from clases.personas import persona

class Profesor(persona):
    
    def __innit__(self):
        super().__init__()
        
        
    def leerDatosProfesor(self):
        self.clave = input("Clave: ")
        
    def mostrarDatosProfesor(self):
        print(self.clave)