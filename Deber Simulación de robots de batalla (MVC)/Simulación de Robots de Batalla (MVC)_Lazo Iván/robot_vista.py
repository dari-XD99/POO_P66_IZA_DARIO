def mostrar_estado(robot):
    print(f"🤖 {robot.nombre} | Energía: {robot.energia} | Estado: {robot.estado}")

def mostrar_combate(atacante, defensor, danio):
    print(f"⚔️ {atacante.nombre} ataca a {defensor.nombre} con {danio} de daño!")

def mostrar_reporte_final(robots, total_rondas):
    print("\n📊 Reporte final del torneo:")
    print(f"🔁 Rondas jugadas: {total_rondas}")
    print("-------------------------------------------------")
    for robot in robots:
        print(f"🤖 {robot.nombre}")
        print(f"   🔋 Energía restante: {robot.energia}")
        print(f"   🛡️ Daño recibido: {robot.danio_recibido}")
        print(f"   💥 Daño infligido: {robot.danio_infligido}")
        print("-------------------------------------------------")
    vivos = [r for r in robots if r.estado == "Activo"]
    if len(vivos) == 1:
        print(f"🏆 ¡El ganador es {vivos[0].nombre}!")
    elif len(vivos) > 1:
        print("El torneo terminó sin un único ganador.")
    else:
        print(" :( Todos los robots fueron destruidos.")
