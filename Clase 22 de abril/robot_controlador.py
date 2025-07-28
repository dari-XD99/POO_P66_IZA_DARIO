"""
Created on Tue Apr 22 09:52:17 2025

@author: jdomi
"""
from robot_modelo import Robot
from robot_vista import mostrar_estado, mostrar_combate
import random
import time

# Crear robots
robot1 = Robot("AlphaX", 100)
robot2 = Robot("OmegaZ", 100)

# Mostrar estado inicial
mostrar_estado(robot1)
mostrar_estado(robot2)

# Múltiples rondas de batalla
print("\n🤖 Inicia la batalla!")
for ronda in range(1, 10):
    print(f"\n🔁 Ronda {ronda}")
    atacante, defensor = (robot1, robot2) if random.choice([True, False]) else (robot2, robot1)
    danio = random.randint(10, 40)
    mostrar_combate(atacante, defensor, danio)
    defensor.recibir_danio(danio)
    mostrar_estado(defensor)
    time.sleep(1)
    if defensor.estado == "Destruido":
        print(f"🏆 {atacante.nombre} ha ganado la batalla!")
        break
