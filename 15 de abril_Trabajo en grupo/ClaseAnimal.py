# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:27:56 2025

@author: lab
"""

class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color

    def comer(self):
        print("comer() ejecutado")

    def moverse(self):
        print("moverse() ejecutado")

# Ejemplo de uso:
animal = Animal("Delphinapterus leucas", "6 años", "Blanco")
print(animal.__dict__)