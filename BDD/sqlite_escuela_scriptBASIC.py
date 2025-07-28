import sqlite3
import os

db_filename = "escuela.db"


db_exists = os.path.exists(db_filename)


conn = sqlite3.connect(db_filename)
cursor = conn.cursor()


if not db_exists:
    cursor.executescript("""
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS carrera (
      clave_c INTEGER PRIMARY KEY,
      nom_c   TEXT,
      durac_c REAL
    );

    CREATE TABLE IF NOT EXISTS materia (
      clave_m INTEGER PRIMARY KEY,
      nom_m   TEXT,
      cred_m  REAL
    );

    CREATE TABLE IF NOT EXISTS profesor (
      clave_p INTEGER PRIMARY KEY,
      nom_p   TEXT,
      dir_p   TEXT,
      tel_p   INTEGER,
      hora_p  TEXT
    );

    CREATE TABLE IF NOT EXISTS alumno (
      mat_alu   INTEGER PRIMARY KEY,
      nom_alu   TEXT,
      edad_alu  INTEGER,
      sem_alu   INTEGER,
      gen_alu   TEXT,
      correo_alu TEXT,
      clave_c1  INTEGER,
      FOREIGN KEY (clave_c1) REFERENCES carrera (clave_c)
    );

    CREATE TABLE IF NOT EXISTS alu_pro (
      mat_alu1 INTEGER,
      clave_p1 INTEGER,
      FOREIGN KEY (mat_alu1) REFERENCES alumno (mat_alu),
      FOREIGN KEY (clave_p1) REFERENCES profesor (clave_p)
    );

    CREATE TABLE IF NOT EXISTS mat_alu (
      mat_alu2 INTEGER,
      clave_m1 INTEGER,
      FOREIGN KEY (mat_alu2) REFERENCES alumno (mat_alu),
      FOREIGN KEY (clave_m1) REFERENCES materia (clave_m)
    );

    CREATE TABLE IF NOT EXISTS mat_pro (
      clave_m2 INTEGER,
      clave_p2 INTEGER,
      FOREIGN KEY (clave_m2) REFERENCES materia (clave_m),
      FOREIGN KEY (clave_p2) REFERENCES profesor (clave_p)
    );

    -- Insertar 10 carreras
    INSERT INTO carrera VALUES
      (1, 'Ingeniería en Sistemas', 9),
      (2, 'Ingeniería Industrial', 10),
      (3, 'Arquitectura', 8),
      (4, 'Medicina', 12),
      (5, 'Derecho', 9),
      (6, 'Psicología', 8),
      (7, 'Comunicación', 7),
      (8, 'Economía', 8),
      (9, 'Biología', 7),
      (10, 'Matemáticas', 6);

    -- Insertar 10 materias
    INSERT INTO materia VALUES
      (101, 'Programación', 5),
      (102, 'Base de Datos', 4),
      (103, 'Cálculo', 6),
      (104, 'Física', 5),
      (105, 'Química', 4),
      (106, 'Ética Profesional', 3),
      (107, 'Psicología General', 4),
      (108, 'Derecho Civil', 5),
      (109, 'Comunicación Oral', 3),
      (110, 'Estadística', 4);

    -- Insertar 10 profesores
    INSERT INTO profesor VALUES
      (1, 'Dra. Ana Torres', 'Calle Falsa 123', 987654321, '2025-06-20 08:00'),
      (2, 'Ing. Luis Pérez', 'Av. Central 456', 987654322, '2025-06-20 09:00'),
      (3, 'Lic. María Gómez', 'Av. Las Flores 789', 987654323, '2025-06-20 10:00'),
      (4, 'Dr. José Martínez', 'Calle Luna 101', 987654324, '2025-06-20 11:00'),
      (5, 'Ing. Carla Mendoza', 'Av. Sol 202', 987654325, '2025-06-20 12:00'),
      (6, 'Lic. Pedro Sánchez', 'Calle Estrella 303', 987654326, '2025-06-20 13:00'),
      (7, 'Dra. Lucía Fernández', 'Av. Mar 404', 987654327, '2025-06-20 14:00'),
      (8, 'Dr. Alberto Ruiz', 'Calle Río 505', 987654328, '2025-06-20 15:00'),
      (9, 'Ing. Sofía Díaz', 'Av. Montaña 606', 987654329, '2025-06-20 16:00'),
      (10, 'Lic. Carlos Ortega', 'Calle Bosque 707', 987654330, '2025-06-20 17:00');

    -- Insertar 10 alumnos (cada uno en una carrera válida)
    INSERT INTO alumno VALUES
      (1001, 'Carlos Ramírez', 20, 4, 'Masculino', 'carlos@example.com', 1),
      (1002, 'Lucía Díaz', 19, 3, 'Femenino', 'lucia@example.com', 2),
      (1003, 'Milena Ortiz', 21, 2, 'Femenino', 'milena@example.com', 3),
      (1004, 'Isaac Mera', 22, 5, 'Masculino', 'isaac@example.com', 4),
      (1005, 'Amy Garcia', 24, 3, 'Femenino', 'amy@example.com', 5),
      (1006, 'Cristian Tipan', 25, 4, 'Masculino', 'cristian@example.com', 6),
      (1007, 'Juan Torres', 23, 7, 'Masculino', 'juan@example.com', 7),
      (1008, 'Lorena Torres', 30, 6, 'Femenino', 'lorena@example.com', 8),
      (1009, 'Jorge Costa', 21, 1, 'Masculino', 'jorge@example.com', 9),
      (1010, 'Alejandra Espinoza', 28, 8, 'Femenino', 'alejandra@example.com', 10);

    -- Relaciones alumno-profesor (asignar 1 profesor a cada alumno)
    INSERT INTO alu_pro VALUES
      (1001, 1),
      (1002, 2),
      (1003, 3),
      (1004, 4),
      (1005, 5),
      (1006, 6),
      (1007, 7),
      (1008, 8),
      (1009, 9),
      (1010, 10);

    -- Relaciones materia-alumno (cada alumno con 1 materia)
    INSERT INTO mat_alu VALUES
      (1001, 101),
      (1002, 102),
      (1003, 103),
      (1004, 104),
      (1005, 105),
      (1006, 106),
      (1007, 107),
      (1008, 108),
      (1009, 109),
      (1010, 110);

    -- Relaciones materia-profesor (cada materia con 1 profesor)
    INSERT INTO mat_pro VALUES
      (101, 1),
      (102, 2),
      (103, 3),
      (104, 4),
      (105, 5),
      (106, 6),
      (107, 7),
      (108, 8),
      (109, 9),
      (110, 10);
    """)
    conn.commit()



print("\nConsulta 1 - Alumnos y Carreras:")
for row in cursor.execute("""
    SELECT a.nom_alu, c.nom_c
    FROM alumno a
    JOIN carrera c ON a.clave_c1 = c.clave_c;
"""):
    print(row)

print("\nConsulta 2 - Profesores y Materias:")
for row in cursor.execute("""
    SELECT p.nom_p, m.nom_m
    FROM mat_pro mp
    JOIN profesor p ON mp.clave_p2 = p.clave_p
    JOIN materia m ON mp.clave_m2 = m.clave_m;
"""):
    print(row)

print("\nConsulta 3 - Alumnos y Materias:")
for row in cursor.execute("""
    SELECT a.nom_alu, m.nom_m
    FROM mat_alu ma
    JOIN alumno a ON ma.mat_alu2 = a.mat_alu
    JOIN materia m ON ma.clave_m1 = m.clave_m;
"""):
    print(row)

print("\nConsulta 4 - Profesores con más de una materia asignada:")
for row in cursor.execute("""
    SELECT p.nom_p, COUNT(mp.clave_m2) AS cantidad_materias
    FROM profesor p
    JOIN mat_pro mp ON p.clave_p = mp.clave_p2
    GROUP BY p.clave_p
    HAVING cantidad_materias > 1;
"""):
    print(row)

print("\nConsulta 5 - Alumnos asignados al profesor con clave_p=1:")
for row in cursor.execute("""
    SELECT a.nom_alu
    FROM alumno a
    JOIN alu_pro ap ON a.mat_alu = ap.mat_alu1
    WHERE ap.clave_p1 = 1;
"""):
    print(row)

print("\nConsulta 6 - Materias con créditos mayores o iguales a 5:")
for row in cursor.execute("""
    SELECT nom_m, cred_m
    FROM materia
    WHERE cred_m >= 5;
"""):
    print(row)

print("\nConsulta 7 - Alumnos y sus profesores:")
for row in cursor.execute("""
    SELECT a.nom_alu, p.nom_p
    FROM alumno a
    JOIN alu_pro ap ON a.mat_alu = ap.mat_alu1
    JOIN profesor p ON ap.clave_p1 = p.clave_p;
"""):
    print(row)

print("\nConsulta 8 - Número de alumnos por carrera:")
for row in cursor.execute("""
    SELECT c.nom_c, COUNT(a.mat_alu) AS total_alumnos
    FROM carrera c
    LEFT JOIN alumno a ON c.clave_c = a.clave_c1
    GROUP BY c.clave_c;
"""):
    print(row)

print("\nConsulta 9 - Materias cursadas por alumnos de la carrera 1:")
for row in cursor.execute("""
    SELECT DISTINCT m.nom_m
    FROM materia m
    JOIN mat_alu ma ON m.clave_m = ma.clave_m1
    JOIN alumno a ON ma.mat_alu2 = a.mat_alu
    WHERE a.clave_c1 = 1;
"""):
    print(row)

print("\nConsulta 10 - Profesores y número de alumnos asignados:")
for row in cursor.execute("""
    SELECT p.nom_p, COUNT(DISTINCT ap.mat_alu1) AS total_alumnos
    FROM profesor p
    LEFT JOIN alu_pro ap ON p.clave_p = ap.clave_p1
    GROUP BY p.clave_p;
"""):
    print(row)

conn.close()
