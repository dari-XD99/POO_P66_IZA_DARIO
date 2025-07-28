# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:30:58 2025

@author: lab
"""

class RedesSociales:
    def __init__(self, nombre, usuarios, publicaciones):
        self.nombre = nombre
        self.usuarios = usuarios
        self.publicaciones = publicaciones

    def agregar_usuario(self):
        print("agregar_usuario() ejecutado")

    def hacer_publicacion(self):
        print("hacer_publicacion() ejecutado")

# Ejemplo de uso:
redessociales = RedesSociales("X antes (Twitter)", "Fulano de tal", "2 fotos")
print(redessociales.__dict__)