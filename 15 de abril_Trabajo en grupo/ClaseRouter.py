# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:35:22 2025

@author: lab
"""

class Router:
    def __init__(self, nombre, ip, estado):
        self.nombre = nombre
        self.ip = ip
        self.estado = estado

    def conectar(self):
        print("conectar() ejecutado")

    def desconectar(self):
        print("desconectar() ejecutado")

# Ejemplo de uso:
router = Router("Wifi_Coffe", "172.17.146.185", "Activo")
print(router.__dict__)