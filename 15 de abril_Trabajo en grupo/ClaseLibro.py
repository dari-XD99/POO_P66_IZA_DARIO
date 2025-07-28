# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:33:54 2025

@author: lab
"""

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def abrir(self):
        print("abrir() ejecutado")

    def leer(self):
        print("leer() ejecutado")

# Ejemplo de uso:
libro = Libro("Probabilidad y estadistica", "Pedro Jose", "729")
print(libro.__dict__)