from datetime import date

class persona:
    def __init__(self,nombre,fechaNac,lugarNac,direccion,telefono,correo):
        self.nombre = nombre
        self.fechaNac = fechaNac
        self.lugarNac = lugarNac
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.rfc = self.generarRFC
        self.__calcularEdad()
        self.rfc = self.generarRFC(self.nombre, self.fechaNac)
    
    def generarRFC(self, nombre, fechaNac):
        fecha_str = [str(fechaNac[0]),str(fechaNac[1]),str(fechaNac[2])]
        if(len(fecha_str[0]) == 1):
            fecha_str[0] == "0" + fecha_str[0]
        if(len(fecha_str[1]) == 1):
            fecha_str[1] == "0" + fecha_str[1]
        return nombre[1][:2] + nombre[2][:1] + nombre[0][:1] + fecha_str[2][-2:] + fecha_str[1] + fecha_str[0]
    
    def __calcularEdad(self):
        self.edad = date.today().year - self.fechaNac[2] - 1
        if(date.today().month > self.fechaNac[1] or (date.today().month == self.fechaNac[1] and date.today().day > self.fechaNac[0])):
            self.edad += 1
    
    def actualizarDatos(self):
        end = False
        while(not end):
            print("1. Dirección")
            print("2. Teléfono")
            print("3. Correo")
            end_opcion = False
            while (not end_opcion):
                opcion = input("Seleccione el dato a actualizar: ")
                if(opcion in "123"):
                    end_opcion = True
                    nuevo_dato = input("Ingrese el nuevo dato: ")
                    if(opcion == "1"):
                        self.direccion = nuevo_dato
                    elif(opcion == "2"):
                        self.telefono = nuevo_dato
                    else:
                        self.correo = nuevo_dato
                    end_od = False
                    while (not end_od):
                        otro_dato = ("¿Desea cambiar otro dato?(1 SÍ, 2 NO): ")
                        if(otro_dato == "2"):
                            end_od = True
                            end = True
                        elif(otro_dato == "1"):
                            end_od = True
                        else:
                            print("Opción no válida.")
                else:
                    print("Opción no válida.")
                    
                
                        

            
            
            
            
            
        