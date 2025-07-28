# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:32:19 2025

@author: lab
"""

class Antena:
    def __init__(self, tipo, frecuencia, potencia):
        self.tipo = tipo
        self.frecuencia = frecuencia
        self.potencia = potencia

    def encender(self):
        print("encender() ejecutado")

    def apagar(self):
        print("apagar() ejecutado")

# Ejemplo de uso:
antena = Antena("Antena direccional", "2.4GHz", "20 dBm")
print(antena.__dict__)