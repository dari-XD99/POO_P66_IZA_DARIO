
# definimos las funciones a usar
def registrar_robots():
    # Pedir al usuario que ingrese el número de robots
    cantidad = int(input("Ingrese el número de robots a registrar: "))
    
    # Verificar que la cantidad sea positiva
    if cantidad <= 0:
        print("Por favor ingrese un número mayor que cero.")
        return
    
    # Diccionario para almacenar los datos de los robots
    robots = {}
    
    # Solicitar datos de cada robot
    for i in range(cantidad):
        nombre = input(f"\nIngrese el nombre del robot {i+1}: ")
        
        # Pedir las 3 lecturas de batería
        lecturas = []
        for j in range(3):
            lectura = float(input(f"Ingrese la lectura {j+1} de batería (0-100%) para {nombre}: "))
            lecturas.append(lectura)
        
        # Calcular promedio de batería
        promedio = j #calcular_promedio(lecturas)
        
        # Determinar estado del robot
        estado = "Operativo" if promedio >= 70 else "Necesita recarga"
        
        # Almacenar datos en el diccionario
        robots[nombre] = {
            'lecturas': lecturas,
            'promedio': promedio,
            'estado': estado
        }
    
    # Ordenar robots por promedio de batería (de mayor a menor)
    robots_ordenados = sorted(robots.items(), key=lambda x: x[1]['promedio'], reverse=True)
    
    # Mostrar resultados
    print("\nReporte de robots (ordenados por batería):")
    print("-" * 50)
    for nombre, datos in robots_ordenados:
        print(f"Robot: {nombre}")
        print(f"Lecturas de batería: {datos['lecturas']}")
        print(f"Promedio de batería: {datos['promedio']:.2f}%")
        print(f"Estado: {datos['estado']}")
        print("-" * 50)
    return sum(lecturas) / len(lecturas)


        
        

        
