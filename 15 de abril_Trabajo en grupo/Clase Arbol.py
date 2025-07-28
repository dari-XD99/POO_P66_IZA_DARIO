# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 09:58:15 2025

@author: lab
"""

class Arbol:
    def __init__(self, especie, altura, edad):
        self.especie = especie
        self.altura = altura
        self.edad = edad
    
    def crecer(self):
        self.altura += 0.5  # Crece medio metro cada año
    
    def producir_oxigeno(self):
        print("Produciendo oxígeno...")
        
arbolF = Arbol("Roble","2 metros", "8")
print(f"Arbol: {arbolF.especie}, Altura: {arbolF.altura}, Edad: {arbolF.edad}") 