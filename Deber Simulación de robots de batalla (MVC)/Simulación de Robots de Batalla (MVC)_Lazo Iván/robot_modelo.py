class Robot:
    def __init__(self, nombre, energia, escudo=0):
        self.nombre = nombre
        self.energia = energia
        self.escudo = escudo  # porcentaje de reducción de daño (0.3 = 30%)
        self.estado = "Activo"
        self.habilidad_usada = False  # para controlar la curación

        # Reporte
        self.danio_infligido = 0
        self.danio_recibido = 0

    def recibir_danio(self, cantidad):
        if self.estado == "Destruido":
            return
        danio_real = int(cantidad * (1 - self.escudo))
        self.energia -= danio_real
        self.danio_recibido += danio_real
        if self.energia <= 0:
            self.energia = 0
            self.estado = "Destruido"

    def usar_habilidad(self):
        if not self.habilidad_usada and self.estado == "Activo":
            self.energia += 25
            self.habilidad_usada = True
            print(f"✨ {self.nombre} usó su habilidad especial: +25 de energía")
