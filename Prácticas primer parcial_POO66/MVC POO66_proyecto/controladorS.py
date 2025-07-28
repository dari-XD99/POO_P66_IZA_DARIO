from modeloS import SistemaSensorial

class Controlador:
    def __init__(self):
        self.sistema = SistemaSensorial()

    def obtener_datos_ambiente(self):
        temp, hum = self.sistema.leer_temperatura_humedad()
        if temp is not None and temp > self.sistema.umbral_temp:
            self.sistema.encender_led()
        else:
            self.sistema.apagar_led()
        return temp, hum

    def obtener_estado_suelo(self):
        return self.sistema.leer_suelo()

    def abrir_ventana(self):
        self.sistema.abrir_ventana()

    def cerrar_ventana(self):
        self.sistema.cerrar_ventana()

    def limpiar(self):
        self.sistema.limpiar()