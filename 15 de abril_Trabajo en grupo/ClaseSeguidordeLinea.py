# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:34:31 2025

@author: lab
"""

class SeguidorLinea:
    def __init__(self, velocidad, posicion):
        self.velocidad = velocidad
        self.posicion = posicion

    def mover(self):
        print("mover() ejecutado")

    def seguir_linea(self):
        print("seguir_linea() ejecutado")

# Ejemplo de uso:
seguidorlinea = SeguidorLinea("0.5 m/s", "Desviado a la derecha")
print(seguidorlinea.__dict__)