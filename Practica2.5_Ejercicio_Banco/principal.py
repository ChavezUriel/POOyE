import persona as p
import cuenta_bancaria as cb
import random

def menu():
    cuentas = inicializarRegistro("clientes.csv")
    end = False
    while (not end):
        print("")
        print("MENÚ PRINCIPAL")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Realizar operación en cuenta")
        print("4. Guardar registros (no funciona)")
        print("0. Salir")
        
        end_opcion = False
        while (not end_opcion):
            opcion = input("Seleccione una opción: ")
            print("")
            if(opcion in "1234"):
                end_opcion = True
                if(opcion == "1"):
                    registroCliente(cuentas)
                elif(opcion == "2"):
                    mostrarUsuarios(cuentas)
                elif(opcion == "3"):
                    print("op3")
                else:
                    print("op4")
            elif(opcion == "0"):
                end_opcion = True
                end = True
                print("Saliendo.")
            else:
                print("Opción no válida.\n")

def inicializarRegistro(path):
    cuentas = []
    with open(path, 'r', encoding="utf-8-sig") as dataShop:
        for line in dataShop:
            line = line.strip()
            line = line.split(",")
            per_obj = p.persona([line[0],line[1],line[2]],[int(line[3]),int(line[4]),int(line[5])],line[6],line[7],line[8],line[9])
            cuenta_obj = cb.CuentaBancaria(line[10],per_obj,float(line[11]))
            cuentas.append(cuenta_obj)
    return  cuentas

def registroCliente(cuentas):
    print("\nNOMBRE")
    nombre = input("Nombre(s) propio: ")
    apep = input("Apellido paterno: ")
    apem = input("Apellido materno: ")
    print("INFORMACIÓN DE NACIMIENTO")
    fnacanio = int(input("Año: "))
    fnacames = int(input("Mes: "))
    fnacdia = int(input("Día: "))
    lnac = input("Lugar: ")
    print("INFORMACIÓN ADICIONAL")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    saldo = float(input("\nIngrese el saldo inicial de la cuenta: "))
    persona_obj = p.persona([nombre,apep,apem],[fnacdia,fnacames,fnacanio],lnac,direccion,telefono,correo)
    numerosusados = []
    for i in range(len(cuentas)):
        numerosusados.append(cuentas[i].numero)
    numero_generado = numerosusados[0]
    while(numero_generado in numerosusados):
        numero_generado = generarNumero()
    cuenta_obj = cb.CuentaBancaria(numero_generado,persona_obj,saldo)
    cuentas.append(cuenta_obj)
    
def generarNumero():
    numero = []
    for i in range(8):
        numero.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
    return numero

def mostrarUsuarios(cuentas):
    print('{:25}{:10}{:10}{:12}{:25}{:13}{:10}'.format("NOMBRE","CUENTA", "SALDO", "RFC", "DIRECCION", "TELFONO", "CORREO"))
    for i in range(len(cuentas)):
        nombre = cuentas[i].cliente.nombre[0] + " " + cuentas[i].cliente.nombre[1] + " " + cuentas[i].cliente.nombre[2]
        print('{:25}{:10}{:10}{:12}{:25}{:13}{:10}'.format(nombre, cuentas[i].numero, str(cuentas[i].saldo), cuentas[i].cliente.rfc, cuentas[i].cliente.direccion, cuentas[i].cliente.telefono, cuentas[i].cliente.correo))        

def realizarOperacion(cuentas):
    ncuentas = []
    for i in range(len(cuentas)):
        ncuentas.append(cuentas[i].numero)
    ncuenta = ncuentas[0]
    while(ncuenta in ncuentas):
        ncuenta = input("Ingrese el núkero de cuenta: ")
        if(ncuenta in ncuentas):
            for i in range(len(cuentas)):
                if(ncuenta == cuentas[i].numero):
                    break
            movimiento = float(input("Ingrese el movimiento (negativo para retiros):"))
            cuentas[i].saldo += movimiento
            print("Movimiento registrado exitosamente")


menu()