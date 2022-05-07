from attr import asdict
from clases import *

# DECLARACIÓN CLIENTES
clientes_lista = []
clientes_lista.append(cliente("Uriel","chavezU@gmail.com",1))
clientes_lista.append(cliente("Valeria","carlos@gmail.com",2))
clientes_lista.append(cliente("Karla","karla_23J@gmail.com",2))
clientes_lista.append(cliente("Eric","ericruiz@gmail.com",3)) 
clientes = {}
for i in range(len(clientes_lista)):
    clientes[clientes_lista[i].NoCliente] = clientes_lista[i]


# DECLARACIÓN EMPLEADOS
empleados_lista = []
empleados_lista.append(empleado("Juan Perez", [5, 8, 1982], "Electrónica",10000))
empleados_lista.append(empleado("Luis Lopez", [8, 11, 1988], "Papelería",5890))
empleados_lista.append(empleado("Maria García", [2,9,1990],"Ropa",12000))
empleados = {}
for i in range(len(empleados_lista)):
    empleados[empleados_lista[i].NoEmpleado] = empleados_lista[i]


# DECLARACIÓN PRODUCTOS
productos_lista = []
productos_lista.append(producto("SONY", 3500, 4))
productos_lista.append(producto("Samsung", 5000, 10))
productos_lista.append(producto("Xiaomi", 9300, 7))
productos_lista.append(producto("Lanix", 3800, 9))
productos_lista.append(producto("HP", 18800, 3))
productos = {}
for i in range(len(productos_lista)):
    productos[productos_lista[i].numero] = productos_lista[i]

# DECLARACIÓN DE DICCIONARIO VACÍO DE VENTAS
ventas = {}


# FUNCIONES DE IMPRESIÓN DE DICCIONARIOS DE OBJETOS

def imprimir_productos(productos):
    print("\n{:10}{:15}{:15}{:20}{:15}".format("ID","Marca","Precio","Precio promoción","Existencias"))
    for i in list(productos.keys()):
        print("{:10}{:15}{:15}{:20}{:15}".format(productos[i].numero,productos[i].marca,str(productos[i].precio),str(productos[i].precio_descuentos),str(productos[i].existencias)))

def imprimir_clientes(clientes):
    print("\n{:10}{:15}{:25}{:10}".format("Numero", "Nombre", "Correo", "Membresía"))
    for i in list(clientes.keys()):
        print("{:10}{:15}{:25}{:10}".format(clientes[i].NoCliente, clientes[i].nombre, clientes[i].correo, clientes[i].tipoCliente))

def imprimir_empleados(empleados):
    print("\n{:15}{:15}{:20}{:15}{:10}".format("Numero", "Nombre", "Fecha nacimiento", "Departamento", "Ventas actuales"))
    for i in list(empleados.keys()):
        fecha = str(empleados[i].fecNac[0]) + "/" + str(empleados[i].fecNac[1]) + "/" + str(empleados[i].fecNac[2])
        print("{:15}{:15}{:20}{:15}{:10}".format(empleados[i].NoEmpleado, empleados[i].nombre, fecha, empleados[i].departamento, str(empleados[i].ventasActuales)))

def imprimir_empleados_sueldos(empleados):
    print("\n{:15}{:15}{:10}".format("Numero", "Nombre", "Sueldo"))
    for i in list(empleados.keys()):
        sueldo = empleados[i].CalcularSueldo()
        print("{:15}{:15}{:10}".format(empleados[i].NoEmpleado, empleados[i].nombre, str(sueldo)))

def imprimir_ventas(ventas):
    print("\n{:15}{:10}{:10}{:10}{:15}{:15}".format("ID Producto","Cantidad", "Descuento", "Total", "ID Vendedor","ID Cliente"))
    for i in list(ventas.keys()):
        print("{:15}{:10}{:10}{:10}{:15}{:15}".format(ventas[i].ID_producto, str(ventas[i].cantidad), str(int(100*ventas[i].descuento))+"%" ,str(ventas[i].CalcularTotalPagar()), ventas[i].ID_vendedor,ventas[i].ID_cliente))

# MENU PRINCIPAL
def menu():
    fin = False
    while(not fin):
        print("\nMENU")
        print("Para salir ingrese 'EXIT'.")
        print("1. Mostrar Clientes")
        print("2. Area administrativa")
        print("3. Registrar venta")
        fin_input = False
        while(not fin_input):
            opcion = input("Seleccione una opción: ")
            if(opcion.lower() == "exit"):
                fin_input = True
                fin = True
            elif(opcion in "123"):
                fin_input = True
                if(opcion == "1"):
                    imprimir_clientes(clientes)
                elif(opcion == "2"):
                    menuAdmin(empleados)
                else:
                    registrarVenta(ventas, empleados, clientes, productos)
            else:
                print("Opción no válida")

# MENU DE ÁREA ADMINISTRATIVA
def menuAdmin(empleados):
    fin = False
    while(not fin):
        print("\nMENU DE ÁREA ADMINISTRATIVA")
        print("Para salir ingrese 'EXIT'.")
        print("1. Mostrar Empleados")
        print("2. Calcular Sueldos")
        fin_input = False
        while(not fin_input):
            opcion = input("Seleccione una opción: ")
            if(opcion.lower() == "exit"):
                fin_input = True
                fin = True
            elif(opcion in "12"):
                fin_input = True
                if(opcion == "1"):
                    imprimir_empleados(empleados)
                else:
                    imprimir_empleados_sueldos(empleados)
            else:
                print("Opción no válida")

# REGISTRO DE VENTAS

def registrarVenta(ventas, empleados, clientes, productos):
    print("\nREGISTRO DE VENTA EN PROCESO")
    print("Para salir en cualquier momento ingrese 'EXIT'.")
    
    imprimir_productos(productos)
    
    fin = False
    while(True):
        ID_producto = input("\nID del producto: ")
        if(ID_producto.lower() == "exit"):
            fin = True
            break
        elif(not ID_producto in list(productos.keys())):
            print("ID de producto no válida.")
        else:
            if(productos[ID_producto].existencias == 0):
                print("No quedan productos en existencia")
                fin = True
                break
            else:
                print("Quedan " + str(productos[ID_producto].existencias) + " productos en existencia.")
                break
    
    if(fin):
        return 0
    
    while(True):
        cantidad = input("\nCantidad: ")
        if(cantidad.lower() == "exit"):
            fin = True
            break
        elif(int(cantidad) > productos[ID_producto].existencias):
            print("La cantidad ingresada excede las existencias.")
        else:
            break
    
    if(fin):
        return 0
    
    imprimir_clientes(clientes)
    
    while(True):
        ID_cliente = input("\nID del cliente: ")
        if(ID_cliente.lower() == "exit"):
            fin = True
            break
        elif(not ID_cliente in list(clientes.keys())):
            print("ID de cliente no válida.")
        else:
            break   
    
    if(fin):
        return 0
    
    imprimir_empleados(empleados)
    
    while(True):
        ID_vendedor = input("\nID del vendedor: ")
        if(ID_vendedor.lower() == "exit"):
            fin = True
            break
        elif(not ID_vendedor in list(empleados.keys())):
            print("ID de empleado no válida.")
        else:
            break
    
    if(fin):
        return 0
    
    ventaReg = venta(int(cantidad), ID_producto, ID_vendedor, ID_cliente, clientes, productos)
    ventas[len(ventas)] = ventaReg
    print("\n Venta registrada con éxito.")
    imprimir_ventas(ventas)


menu()

