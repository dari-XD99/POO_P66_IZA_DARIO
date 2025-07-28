# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:29:26 2025

@author: lab
"""

class DispositivoIoT:
    def __init__(self, ID, tipo, estado):
        self.ID = ID
        self.tipo = tipo
        self.estado = estado

    def encender(self):
        print("encender() ejecutado")

    def apagar(self):
        print("apagar() ejecutado")

# Ejemplo de uso:
dispositivoiot = DispositivoIoT("device-1234", "Sensor", "Encendido")
print(dispositivoiot.__dict__)