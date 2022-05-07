import random

class producto:
    def __init__(self,marca,precio,existencias):
        self.numero = self.GenerarID()
        self.marca = marca
        self.precio = precio
        self.precio_descuentos = precio
        self.existencias = existencias
    
    def GenerarID(self):
        mayusculas = "QWERTYUIOPASDFGHJKLZXCVBNM"
        digitos = "123456789"
        vocalMin = "aeiou"
        ID = random.choice(mayusculas) + random.choice(digitos) + random.choice(digitos) + random.choice(vocalMin) + random.choice(digitos) + random.choice(digitos)
        return ID
    
    def actualizarExistencias(self, cambio):
        if(self.existencias + cambio < 0):
            print("No hay suficientes productos en existencia")
        else:
            self.existencias += cambio
    
    def ModificarPrecio(self,nuevoPrecio):
        self.precio = nuevoPrecio
        self.precio_descuentos = nuevoPrecio
    
    def aplicarDescuento(self,porcentajeDescuento):
        self.precio_descuentos = self.precio * (100 - porcentajeDescuento) / 100


class cliente:
    def __init__(self, nombre, correo, tipoCliente):
        self.NoCliente = self.GenerarNumeroCliente()
        self.nombre = nombre
        self.correo = correo
        tipos = ["Oro", "Plata", "Bronce"]
        self.tipoCliente = tipos[tipoCliente-1]
        
    def GenerarNumeroCliente(self):
        caracteres = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        numero = ""
        for i in range(8):
            numero += random.choice(caracteres)
        return numero

    def ModificarCorreoElectronico(self):
        correo = input("Ingrese el nuevo correo electrónico: ")
        self.correo = correo

    def ActualizarTipoCliente(self, tipo = 0):
        tipos = ["Oro", "Plata", "Bronce"]
        if(str(tipo) in "123"):
            self.tipoCliente = tipos[tipo-1]
        else:
            fin = False
            while(not fin):
                print("1. Oro")
                print("2. Plata")
                print("3. Bronce")
                tipo = int(input("Seleccione el nuevo tipo de cliente: "))
                if(str(tipo) in "123"):
                    self.tipoCliente = tipos[tipo-1]
                    fin = True
                else:
                    print("Opción no válida.")    

sueldoBase = 8000

class empleado():
    def __init__(self, nombre, fecNac, departamento, ventasActuales):
        self.nombre = nombre
        self.fecNac = fecNac
        self.departamento = departamento
        self.ventasActuales = ventasActuales
        self.NoEmpleado = self.GenerarNumeroEmpleado()
    
    def GenerarNumeroEmpleado(self):
        digitos = "1234567890"
        vocales = "AEIOU"
        numero = self.nombre[1:4].upper() + random.choice(digitos) + random.choice(digitos) + random.choice(digitos) + random.choice(vocales) + random.choice(vocales) + random.choice(digitos) + random.choice(digitos) + self.departamento[:1]
        return numero
        
    def ActualizarVentasTotales(self, venta):
        self.ventasActuales += venta
    
    def CalcularSueldo(self):
        edad = self.__calcularEdad()
        sueldo = sueldoBase + 0.05 * self.ventasActuales
        if(edad >= 50):
            sueldo += 0.015 * sueldoBase
        elif(edad >= 40):
            sueldo += 0.03 * sueldoBase
        elif(edad >= 30):
            sueldo += 0.035 * sueldoBase
        return sueldo
        
    def __calcularEdad(self):
        hoy = [29,4,2022]
        edad = hoy[2] - self.fecNac[2] - 1
        if(hoy[1] > self.fecNac[1] or (hoy[1] == self.fecNac[1] and hoy[0] > self.fecNac[0])):
            edad += 1
        return edad

class venta:
    def __init__(self, cantidad, ID_producto, ID_vendedor, ID_cliente, clientes, productos):
        self.cantidad = cantidad
        self.ID_producto = ID_producto
        self.ID_vendedor = ID_vendedor
        self.ID_cliente = ID_cliente
        descuentos = {"Oro": 0.08, "Plata": 0.05, "Bronce": 0.03}
        self.descuento = descuentos[clientes[ID_cliente].tipoCliente]
        self.producto = productos[ID_producto]

    def CalcularTotalPagar(self):      
        total = self.producto.precio * self.cantidad
        total = total * (1 - self.descuento)
        return total



