import star
import components as co

# MENÚ DE INGRESO DE DATOS
def menu_datos():
    datos = {}
    fin = False
    while (fin == False):
        print('')
        print('MENÚ INGRESO DE DATOS')
        print('Utilice algún número para seleccionar una opción.')
        print('Para salir ingrese "EXIT".')
        print('\t 1. Agregar datos en archivo')
        print('\t 2. Agregar datos manualmente')
        print('\t 3. Mostrar datos actuales')
        print('\t 4. Procesar datos actuales')
        fin_input = False
        while(fin_input == False):
            inp = input('Seleccione la opción deseada: ')
            print("")
            if inp in ['1','2','3','4']:
                fin_input = True
                if inp == '1':
                    datos = ag_datos_archivo(datos)
                elif inp == '2':
                    datos = ag_datos_manual(datos)
                elif inp == '3':
                    if(datos == []):
                        print("Actualmente no hay datos agregados.")
                    else:
                        co.seeStars(datos)
                else:
                    menu_proc(datos)
            elif inp.lower() == 'exit':
                fin_input = True
                fin = True
                print("Cerrando.")
            else:
                print("Opción no válida.")

# AGREGAR DATOS DESDE ARCHIVO
def ag_datos_archivo(datos):
    print("Ingrese solamente el nombre del archivo si se encuentra en")
    print("la misma carpeta en que se está ejecutando este programa.") 
    path = input("Ruta: ")
    datos_arch = co.readData(path)
    datos = appendDict(datos, datos_arch)
    return datos

# AGREGAR DATOS MANUALMENTE
def ag_datos_manual(datos):
    fin = False
    while(not fin):
        print("Objeto #" + str(len(datos)+1) + "")
        inpU = float(input("U = "))
        inpB = float(input("B = "))
        inpV = float(input("V = "))
        datos[len(datos)+1] = co.getStars(inpU,inpB,inpV,star.star.typeStar(inpB,inpV))
        
        fin_preg = False
        while(not fin_preg):
            opcion = input("¿Quiere ingresar más datos?(1 SÍ, 2 NO): ")
            if(opcion in ["1","2"]):
                if(opcion == "2"):
                    fin = True
                fin_preg = True
            else:
                print("Opción no válida.")
    return datos

# AGREGAR ESTRELLA A DICCIONARIO DE ESTRELLAS
def appendDict(dict, data):
    for i in range(len(data)):
        dict[len(dict)+1] = co.getStars(data[i][0],data[i][1],data[i][2],star.star.typeStar(float(data[i][1]),float(data[i][2])))
    return dict

# MENÚ DE PROCESAMIENTO DE DATOS
def menu_proc(datos):
    fin = False
    while (fin == False):
        print('')
        print('MENÚ PROCESAMIENTO DE DATOS')
        print('Utilice algún número para seleccionar una opción.')
        print('Para salir de este menú ingrese "EXIT".')
        print('\t 1. Diagrama de Hertzsprung-Russell')
        print('\t 2. Histograma de frecuencias')
        print('\t 3. Mostrar datos actuales')
        fin_input = False
        while(fin_input == False):
            inp = input('Seleccione la opción deseada: ')
            print("")
            if inp in ['1','2','3']:
                fin_input = True
                if inp == '1':
                    co.Hertzsprung_Russell_Diagram(datos)
                elif inp == '2':
                    co.freqPlot(datos)
                else:
                    if(datos == []):
                        print("Actualmente no hay datos agregados.")
                    else:
                        co.seeStars(datos)
            elif inp.lower() == 'exit':
                fin_input = True
                fin = True
                print("Saliendo del menú de procesamiento de datos.")
            else:
                print("Opción no válida.")


menu_datos()
