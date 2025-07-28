"""
Created on Tue Apr 22 09:52:17 2025

@author: jdomi
"""
def mostrar_estado(robot):
    print(f"🤖 {robot.nombre} | Energía: {robot.energia} | Estado: {robot.estado}")

def mostrar_combate(atacante, defensor, danio):
    print(f"⚔️ {atacante.nombre} ataca a {defensor.nombre} con {danio} de daño!")
