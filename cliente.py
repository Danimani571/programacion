from Empleado import Empleado
class Cliente(Empleado):
    def __init__(self, idcliente, fecharegistro, vip):
        self._idcliente = idcliente
        self._fecharegistro = fecharegistro
        self._vip = vip

    @property
    def idcliente(self):
        return self._idcliente

    @idcliente.setter
    def idcliente(self, nuevo_id):
        self._idcliente = nuevo_id

    @property
    def fecharegistro(self):
        return self._fecharegistro

    @fecharegistro.setter
    def fecharegistro(self, nueva_fecha):
        self._fecharegistro = nueva_fecha

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, nuevo_estado):
        self._vip = nuevo_estado

    def __str__(self):
        vip_str = "VIP" if self._vip else "No VIP"
        return f"Cliente {self._idcliente}: Registrado el {self._fecharegistro} ({vip_str})"

# Ejemplo de uso
cliente1 = Cliente(idcliente=1, fecharegistro="2024-06-12", vip=True)
print(cliente1)



