# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:35:53 2025

@author: lab
"""

class PuntoAccesoAP:
    def __init__(self, ssid, mac, estado):
        self.ssid = ssid
        self.mac = mac
        self.estado = estado

    def activar(self):
        print("activar() ejecutado")

    def desactivar(self):
        print("desactivar() ejecutado")

# Ejemplo de uso:
puntoaccesoap = PuntoAccesoAP("WiFi_Libre", "98:5F:D3:AE:9C:72", "En mantenimiento")
print(puntoaccesoap.__dict__)