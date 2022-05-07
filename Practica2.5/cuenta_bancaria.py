import persona as p

class CuentaBancaria:
    def __init__(self, numero, cliente, saldo):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        
    def ConsultarSaldo(self):
        print("El saldo actual es: " + str(self.saldo))
        
    def ActualizarSaldo(self, movimiento):
        if(self.saldo + movimiento > 0):
            self.saldo += movimiento
        else:
            print("No hay saldo disponible para hacer el movimiento.")
        
    def ActualizarDatosCliente(self):
        self.cliente.actualizarDatos()
