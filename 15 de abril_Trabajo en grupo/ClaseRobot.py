# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:30:24 2025

@author: lab
"""

class Robot:
    def __init__(self, modelo, tarea, bateria):
        self.modelo = modelo
        self.tarea = tarea
        self.bateria = bateria

    def realizar_tarea(self):
        print("realizar_tarea() ejecutado")

    def cargar_bateria(self):
        print("cargar_bateria() ejecutado")

# Ejemplo de uso:
robot = Robot("ARM", "Ordenar cajas", "98%")
print(robot.__dict__)