from robot_modelo import Robot
from robot_vista import mostrar_estado, mostrar_combate, mostrar_reporte_final
import random
import time

# Robots con escudo aleatorio entre 10% y 40%
nombres = ["AlphaX", "OmegaZ", "Atom", "Wall-e"]
robots = []

for nombre in nombres:
    escudo = round(random.uniform(0.1, 0.4), 2)  
    robot = Robot(nombre, energia=100, escudo=escudo)
    robots.append(robot)
    print(f"🤖 {nombre} creado con escudo del {int(escudo * 100)}%")

# Estado inicial
print("\n ESTADO INICIAL DE LOS ROBOTS:")
for r in robots:
    mostrar_estado(r)

# Sorteo
print("\n🎲 Sorteando enfrentamientos de semifinal")
random.shuffle(robots)
rondas = 0
finalistas = []

# SEMIFINALES
for i in range(0, len(robots), 2):
    r1 = robots[i]
    r2 = robots[i+1]
    print(f"\n⚔️ Semifinal: {r1.nombre} vs {r2.nombre}")
    ganador = None
    while r1.estado == "Activo" and r2.estado == "Activo":
        atacante, defensor = (r1, r2) if random.choice([True, False]) else (r2, r1)
        danio = random.randint(10, 35)
        mostrar_combate(atacante, defensor, danio)
        defensor.recibir_danio(danio)
        atacante.danio_infligido += danio
        mostrar_estado(defensor)

        # Habilidad especial
        if defensor.energia <= 30 and not defensor.habilidad_usada:
            defensor.usar_habilidad()
            mostrar_estado(defensor)

        time.sleep(0.99)
        rondas += 1

    ganador = r1 if r1.estado == "Activo" else r2
    finalistas.append(ganador)
    print(f"\n✅ {ganador.nombre} avanza a la FINAL")

# FINAL
print("\n🏁 GRAN FINAL:")
r1, r2 = finalistas
print(f"\n {r1.nombre} vs {r2.nombre}")
while r1.estado == "Activo" and r2.estado == "Activo":
    atacante, defensor = (r1, r2) if random.choice([True, False]) else (r2, r1)
    danio = random.randint(10, 35)
    mostrar_combate(atacante, defensor, danio)
    defensor.recibir_danio(danio)
    atacante.danio_infligido += danio
    mostrar_estado(defensor)

    if defensor.energia <= 30 and not defensor.habilidad_usada:
        defensor.usar_habilidad()
        mostrar_estado(defensor)

    time.sleep(0.5)
    rondas += 1

ganador_final = r1 if r1.estado == "Activo" else r2
print(f"\n🏆 ¡{ganador_final.nombre} gana el torneo!")

# Reporte final
mostrar_reporte_final(robots, rondas)
