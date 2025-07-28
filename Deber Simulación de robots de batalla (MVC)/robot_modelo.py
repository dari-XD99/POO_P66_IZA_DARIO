"""
Created on Tue Apr 22 09:52:17 2025

@author: jdomi
"""
class Robot:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia
        self.estado = "Activo"

    def recibir_danio(self, cantidad):
        if self.estado == "Destruido":
            return
        self.energia -= cantidad
        if self.energia <= 0:
            self.energia = 0
            self.estado = "Destruido"
