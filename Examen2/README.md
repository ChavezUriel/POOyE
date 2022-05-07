Instrucciones 1ra Parte:

Debemos crear las clases necesarias para la administración de una tienda departamental (El problema será definido en la segunda parte del examen). En cada caso, debemos considerar los parámetros que tendrán los métodos de las respectivas clases.

Clase: Producto

Atributos: ID (compuesto por 6 caracteres: 1 letra mayúscula + 2 dígitos + 1 vocal minúscula + 2 dígitos. Se debe generar de forma aleatoria). Marca, Precio, Existencias

Métodos: a) GenerarID(), deberá permitir generar el ID del producto según las especificaciones. b) actualizarExistencias(), deberá realizar la operación de incrementar/disminuir la cantidad de productos. c) ModificarPrecio(), deberá permitir hacer modificaciones en el caso de que exista algún descuento.

Clase: Cliente

Atributos: NoCliente (compuesto por 8 caracteres alfanumericos generados de forma aleatoria), Nombre, Correo Electrónico, TipoCliente (Se tendrán 3: Oro, Plata y Bronce).

Métodos: a) GenerarNumeroCliente(), deberá permitir generar el número de cliente según las especificaciones. b) Modificar Correo electrónico(). c) ActualizarTipoCliente()

Clase: Empleado

Atributos: NoEmpleado(compuesto por 10 caracteres: letras 2,3,4 del nombre del cliente + 3 digitos + 2 vocales + 2 dígitos + primera letra mayúscula del departemento en que trabaja), Nombre, Fecha Nacimiento, Departamento en el que trabaja, VentasActuales.

Métodos: a) GenerarNumeroEmpleado(), deberá permitir generar el número de empleado según las especificaciones, b)ActualizarVentasTotales(), deberá registrar la cantidad de ventas que tiene el empleado. c) CalcularSueldo(), se debe considerar que los empleados tienen un sueldo base más el 5% de comisiones de lo que han vendido + un bono que depende de su edad: mayores de 40 años se suma el 3% del sueldo, mayores de 50 años se suma el 1.5% de su sueldo, menores de 30 años reciben un 3.5%.

Clase: Venta

Atributos: Cantidad, ID producto, IDvendedor, ID cliente y descuento.

Métodos: CalcularTotalPagar() Se deberá calcular la cantidad que va a pagar el cliente, considerando la cantidad de productos que adquirió, así como el descuento al que tiene derecho según el tipo de cliente del que se trata: ORO-8%, Plata-5%, Bronce-3%


Instrucciones 2da Parte:

Utilizando las clases que se crearon en la primera parte del examen, se debe desarrollar un programa que realice lo mencionado en la siguiente lista:

Crear un archivo main, donde se realice lo siguiente:

1. Se deben crear cuatro clientes. Los valores se pueden ingresar desde teclado o bien se pueden colocar en el código.
2. Se deben crear tres empleados: a) Ventas = 10000 - Fecha Nacimiento: 05/08/1982 - Nombre: Juan Perez - Departamento: Electronica b) Ventas: 5890 - Fecha Nacimiento: 08/11/1988 - Nombre: Luis Lopez - Departamento: Papeleria c) Ventas: 12000 - Fecha Nacimiento: 02/09/1990 - Nombre: María García - Departamento: Ropa
3. Se deben crear 5 diferentes productos, inicializando los datos necesarios de forma libre.
4. Crear un menu con las siguientes opciones: 1) Mostrar Clientes, 2) Area Administrativa, 3) Registrar Venta
5. En "área administrativa" se tendrán dos opciones: a) Mostrar Empleados y b) Calcular Sueldos

Se debe considerar que el menú principal se deberá poder ejecutar varias veces durante el día.

Se deberán utilizar funciones, ciclos, condiciones, diccionarios, listas, etc.


Se deberá entregar una carpeta comprimida con los archivos de las clases (de la primera parte del examen) así como los nuevos archivos que se hayan generado.