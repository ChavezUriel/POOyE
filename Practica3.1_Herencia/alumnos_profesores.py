
class obj():
    def __init__(self):
        super(obj,self).__init__()
    

class persona(obj):
    def __init__(self,
                 nombre = "DESCONOCIDO",
                 sexo = "DESCONOCIDO",
                 edad = "DESCONOCIDO",
                 lugNac = "DESCONOCIDO",
                 *args,
                 **kwargs):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.lugNac = lugNac
        super(persona,self).__init__(*args, **kwargs)
    
    def info(self):
        print(
            "\nNombre: ", self.nombre,
            "\nSexo: ", self.sexo,
            "\nEdad: ", self.edad,
            "\nLugar de nacimiento: ", self.lugNac
        )


class destreza(obj):
    def __init__(self,
                 mejor_materia = "DESCONOCIDA",
                 peor_materia = "DESCONOCIDA",
                 *args,
                 **kwargs):
        self.mejor_materia = mejor_materia
        self.peor_materia = peor_materia
        super(destreza, self).__init__(*args, **kwargs)
    
    def info(self):
        print(
            "\nMejor materia: ", self.mejor_materia,
            "\nPeor materia: ", self.peor_materia
        )

class alumno(persona, destreza):
    def __init__(self,
                 NUA = "DESCONOCIDO", 
                 semestre = "DESCONOCIDO", 
                 promedio = "DESCONOCIDO", 
                 carrera = "DESCONOCIDO", 
                 *args, 
                 **kwargs):
        self.NUA = NUA
        self.semestre = semestre
        self.promedio = promedio
        self.carrera = carrera
        super(alumno,self).__init__(*args, **kwargs)
    
    def info(self):
        print("\n")
        persona.info(self)
        destreza.info(self)
        print(
            "\nNUA: ", self.NUA,
            "\nSemestre: ", self.semestre,
            "\nPromedio: ", self.promedio,
            "\nCarrera: ", self.carrera
        )

class profesor(persona, destreza):
    def __init__(self, 
                 NUE = "DESCONOCIDO", 
                 antiguedad = "DESCONOCIDO", 
                 horasLab = "DESCONOCIDO", 
                 grado = "DESCONOCIDO", 
                 *args, 
                 **kwargs):
        self.NUE = NUE
        self.antiguedad = antiguedad
        self.horasLab = horasLab
        self.grado = grado
        super(profesor, self).__init__(*args, **kwargs)
    
    def info(self):
        print("\n")
        persona.info(self)
        destreza.info(self)
        print(
            "\nNUE: ", self.NUE,
            "\nAntigüedad: ", self.antiguedad,
            "\nHoras laboradas: ", self.horasLab,
            "\nGrado: ", self.grado
        )


alumno1 = alumno(427086,
                 8,
                 9.01,
                 "Licenciatura en Física",
                 "Uriel Chávez Flores",
                 "Masculino",
                 21,
                 "Aguascalientes, Aguascalientes",
                 "POOyE",
                 "Cosmología")
alumno1.info()

profesor1 = profesor(301580,
                     4,
                     15,
                     "Maestría",
                     "Eric Ruiz Flores",
                     "Masculino",
                     24,
                     "Aguascalientes, Aguascalientes",
                     "Sistemas Lineales",
                     "POOyE")
profesor1.info()

alumno2 = alumno(sexo = "Femenino",
                 NUA = 426062,
                 peor_materia = "Métodos Numéricos",
                 semestre = 10,
                 lugNac = "Leon, Gto.",
                 nombre = "Fernanda Guerrero Aguilar",
                 mejor_materia = "Análisis Tensorial")
alumno2.info()

print("\n")

