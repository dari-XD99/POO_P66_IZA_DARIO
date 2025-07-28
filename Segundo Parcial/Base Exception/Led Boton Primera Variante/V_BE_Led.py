class VistaLed:
    def mostrar_estado_led(self, encendido):
        print("LED encendido" if encendido else "LED apagado")

    def mostrar_error_comando(self):
        print("Comando inválido, por favor utilizar el correcto.")

    def mostrar_modo(self, modo):
        print(f"Modo actual: {'CONTROL POR COMANDOS' if modo == 'comando' else 'CONTROL POR BOTÓN'}")
