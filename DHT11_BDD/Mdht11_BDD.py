import sqlite3
from datetime import datetime
import dht11
import RPi.GPIO as GPIO
import logging

class SensorDHT11:
    def __init__(self, pin=4):  
        GPIO.setmode(GPIO.BCM)
        self.instance = dht11.DHT11(pin=self.pin)
        self.logger = logging.getLogger('SensorDHT11')
    
    def leer_datos(self):
        try:
            result = self.instance.read()
            if result.is_valid():
                return {
                    'temperatura': result.temperature,
                    'humedad': result.humidity,
                    'timestamp': datetime.now(),
                    'estado': 'Crítico' if result.temperature > 30 or result.humidity < 30 else 'Normal'
                }
            raise Exception("Error de lectura del sensor")
        except Exception as e:
            self.logger.error(f"Error en sensor DHT11: {str(e)}")
            return None
        finally:
            GPIO.cleanup()

class BaseDeDatos:
    def __init__(self, db_name='monitoreo.db'):
        self.conn = sqlite3.connect(db_name)
        self._crear_tablas()
    
    def _crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL NOT NULL,
            humedad REAL NOT NULL,
            fecha_hora TEXT NOT NULL,
            estado TEXT NOT NULL
        )
        ''')
        self.conn.commit()
    
    def guardar_lectura(self, datos):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO lecturas (temperatura, humedad, fecha_hora, estado)
        VALUES (?, ?, ?, ?)
        ''', (datos['temperatura'], datos['humedad'], 
              datos['timestamp'].strftime('%Y-%m-%d %H:%M:%S'), 
              datos['estado']))
        self.conn.commit()
    
    def obtener_lecturas(self, limite=10):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT * FROM lecturas 
        ORDER BY fecha_hora DESC 
        LIMIT ?
        ''', (limite,))
        return cursor.fetchall()
    
    def cerrar(self):
        self.conn.close()
