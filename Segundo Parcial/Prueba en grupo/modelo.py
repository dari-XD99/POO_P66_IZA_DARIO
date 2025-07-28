import sqlite3
from datetime import datetime

class BaseDatos:
    def __init__(self, db_name="base_datos.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor (
            id_sensor INTEGER PRIMARY KEY AUTOINCREMENT,
            ubicacion TEXT,
            tipo TEXT,
            estado TEXT
        )''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS lectura (
            id_lectura INTEGER PRIMARY KEY AUTOINCREMENT,
            id_sensor INTEGER,
            temperatura REAL,
            humedad REAL,
            fecha_hora TEXT,
            estado TEXT,
            FOREIGN KEY (id_sensor) REFERENCES sensor(id_sensor)
        )''')
        self.conn.commit()

        
        self.cursor.execute("SELECT COUNT(*) FROM sensor")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO sensor (ubicacion, tipo, estado) VALUES (?, ?, ?)",
                                ("Laboratorio", "DHT11", "activo"))
            self.conn.commit()

    def insertar_lectura(self, id_sensor, temperatura, humedad, estado):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO lectura (id_sensor, temperatura, humedad, fecha_hora, estado)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_sensor, temperatura, humedad, fecha_hora, estado))
        self.conn.commit()
