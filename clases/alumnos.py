from clases.personas import persona

class Alumno(persona):
    def __innit__(self):
        super().__init__()
        self.cuenta = ""
        
    def leerDatosAlumno(self):
        self.cuenta = input("Cuenta: ")
        
    def mostrarResultadoAlumno(self):
        print(self.cuenta)