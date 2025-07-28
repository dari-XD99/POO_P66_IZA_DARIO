# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:21:05 2025

@author: lab
"""

class Cine:
    def __init__(self, nombre, ubicacion, numero_salas):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.numero_salas = numero_salas

    def mostrar_peliculas(self):
        print("mostrar_peliculas() ejecutado")

# Ejemplo de uso:
cine = Cine("Multicines", "Quicentro Sur", "11")
print(cine.__dict__)