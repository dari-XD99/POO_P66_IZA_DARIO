import threading
import time
from modelos.Mdht11_BDD import SensorDHT11, BaseDeDatos

class ControladorMonitor:
    def __init__(self):
        self.sensor = SensorDHT11(pin=4) 
        self.bd = BaseDeDatos()
        self.monitoreo_activo = False
        self.hilo_monitoreo = None
    
    def iniciar_monitoreo(self, intervalo=5):
        if not self.monitoreo_activo:
            self.monitoreo_activo = True
            self.hilo_monitoreo = threading.Thread(
                target=self._bucle_monitoreo,
                args=(intervalo,),
                daemon=True
            )
            self.hilo_monitoreo.start()
    
    def detener_monitoreo(self):
        self.monitoreo_activo = False
        if self.hilo_monitoreo:
            self.hilo_monitoreo.join()
    
    def _bucle_monitoreo(self, intervalo):
        while self.monitoreo_activo:
            datos = self.sensor.leer_datos()
            if datos:
                self.bd.guardar_lectura(datos)
            time.sleep(intervalo)
    
    def obtener_lecturas(self, limite=10):
        return self.bd.obtener_lecturas(limite)
    
    def cerrar(self):
        self.detener_monitoreo()
        self.bd.cerrar()
