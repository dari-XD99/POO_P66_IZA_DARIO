# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:28:47 2025

@author: lab
"""

class Coche:
    def __init__(self, modelo, color, velocidad_maxima):
        self.modelo = modelo
        self.color = color
        self.velocidad_maxima = velocidad_maxima

    def encender(self):
        print("encender() ejecutado")

    def acelerar(self):
        print("acelerar() ejecutado")

# Ejemplo de uso:
coche = Coche("Made in China", "Nacarado", "120 Km/h")
print(coche.__dict__)