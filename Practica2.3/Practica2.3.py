import matplotlib.pyplot as plt
import numpy as np

class archivos:
    # Para inicializar el objeto se lee un archivo con el método actualizarContenido
    # y se guarda como un atributo self.contenido
    def __init__(self,ruta,nombreArchivo):
        self.contenido = self.actualizarContenido(ruta, nombreArchivo)
    
    # Método para actualizar e inicializar el atributo de contenido del archivo
    def actualizarContenido(self, ruta, nombreArchivo):
        contenido = ""
        with open(ruta + nombreArchivo, "r") as file:
            for line in file:
                contenido = contenido + line + " "
        self.contenido = contenido
        return contenido
    
    # Se hace el conteo de las palabras indicadas primero eliminando los caracteres
    # que no son alfanuméricos y luego dividiendo en palabras
    # Para el histograma se usa plt.bar() que a diferencia de plt.hist recibe las
    # alturas o frecuencias de clase y las clases como argumento
    def conteoHistograma(self):       
        contenidoLimpio = ""
        for letra in self.contenido:
            if(letra.isalnum()):
                contenidoLimpio += letra
            else:
                contenidoLimpio += " "
        palabras = contenidoLimpio.split(" ")
        datos = {"the":0 ,"and":0, "it":0, "in":0, "on":0}
        for palabra in palabras:
            if(palabra in datos.keys()):
                datos[palabra] += 1
        plt.bar(datos.keys(), datos.values())
        plt.show()
    
    # Funciones de conteo
    
    def conteoVocales(self):
        conteo = 0
        for letra in self.contenido:
            if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
                conteo += 1
        return conteo
    
    def conteoFrases(self):
        return len(self.contenido.split("."))
    
    def conteoMayusculas(self):
        conteo = 0
        for letra in self.contenido:
            if(letra.isupper()):
                conteo += 1
        return conteo
        

ruta = ""
nombreArchivo = "mexico.txt"

# Declaración del objeto
f1 = archivos(ruta, nombreArchivo)

# Usamos los métodos hechos
vocales = f1.conteoVocales()
frases = f1.conteoFrases()
mayusculas = f1.conteoMayusculas()
f1.conteoHistograma()

# Guardamos los conteos hechos
f2 = open("Contadores.txt", "w")
f2.write("Conteo")
f2.write("\nVocales: " + str(vocales))
f2.write("\nFrases: " + str(frases))
f2.write("\nMayusculas: " + str(mayusculas))
f2.close() 

