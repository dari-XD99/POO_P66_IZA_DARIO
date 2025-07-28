# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:33:18 2025

@author: lab
"""

class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def jugar(self):
        print("jugar() ejecutado")

    def alimentar(self):
        print("alimentar() ejecutado")

# Ejemplo de uso:
mascota = Mascota("Tobby", "Caniche", "8 años")
print(mascota.__dict__)