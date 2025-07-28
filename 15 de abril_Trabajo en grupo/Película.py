# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:06:31 2025

@author: lab
"""


class Película:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def reproducir(self):
        print("reproducir() ejecutado")

    def obtener_duracion(self):
        print("obtener_duracion() ejecutado")

película = Película("Isaac Criminal de Mexico", "1 hora y 30 minutos", "Drama")
print(película.__dict__)
