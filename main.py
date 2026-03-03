
from clases.alumnos import Alumno
from clases.profesores import Profesor 
from clases.exalumnos import Exalumno

def main():
    
    al = Alumno()
    al.leerDatosPersona()
    al.leerDatosAlumno()
    al.mostrarDatosPersona()
    al.mostrarDatosPersona()
    
    prof = Profesor()
    prof.leerDatosProfesor()
    prof.mostrarDatosProfesor()
    
    exa= Exalumno()
    exa.leerDatosPersona()
    exa.leerDatosAlumno()
    exa.leerDatosProfesor()
    exa.leerDatosExalumno()
    print("********************")
    exa.mostrarDatosPersona()
    exa.mostrarResultadoAlumno()
    exa.mostrarDatosProfesor()
    exa.mostrarDatosExalumno()
    
if __name__ == "__main__":
    main()