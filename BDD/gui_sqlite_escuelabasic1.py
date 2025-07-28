import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

DB_NAME = "escuela.db"

# Función para ejecutar consultas
def execute_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Función para obtener resultados de consulta
def fetch_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Funciones de operación
def insertar_alumno():
    datos = (entry_mat.get(), entry_nom.get(), entry_edad.get(), entry_sem.get(),
             entry_gen.get(), entry_correo.get(), entry_carrera.get())
    query = "INSERT INTO alumno VALUES (?, ?, ?, ?, ?, ?, ?)"
    try:
        execute_query(query, datos)
        messagebox.showinfo("Éxito", "Alumno insertado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_alumno():
    mat = entry_mat.get()
    query = "DELETE FROM alumno WHERE mat_alu = ?"
    execute_query(query, (mat,))
    messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")

def consultar_alumnos():
    for row in tree.get_children():
        tree.delete(row)
    query = "SELECT mat_alu, nom_alu, correo_alu FROM alumno"
    for alumno in fetch_query(query):
        tree.insert('', 'end', values=alumno)

# GUI principal
root = tk.Tk()
root.title("Gestión de Alumnos - Escuela")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Matrícula").grid(row=0, column=0)
entry_mat = tk.Entry(frame)
entry_mat.grid(row=0, column=1)

tk.Label(frame, text="Nombre").grid(row=1, column=0)
entry_nom = tk.Entry(frame)
entry_nom.grid(row=1, column=1)

tk.Label(frame, text="Edad").grid(row=2, column=0)
entry_edad = tk.Entry(frame)
entry_edad.grid(row=2, column=1)

tk.Label(frame, text="Semestre").grid(row=3, column=0)
entry_sem = tk.Entry(frame)
entry_sem.grid(row=3, column=1)

tk.Label(frame, text="Género").grid(row=4, column=0)
entry_gen = tk.Entry(frame)
entry_gen.grid(row=4, column=1)

tk.Label(frame, text="Correo").grid(row=5, column=0)
entry_correo = tk.Entry(frame)
entry_correo.grid(row=5, column=1)

tk.Label(frame, text="Clave Carrera").grid(row=6, column=0)
entry_carrera = tk.Entry(frame)
entry_carrera.grid(row=6, column=1)

btn_insertar = tk.Button(frame, text="Insertar", command=insertar_alumno)
btn_insertar.grid(row=7, column=0, pady=5)

btn_eliminar = tk.Button(frame, text="Eliminar", command=eliminar_alumno)
btn_eliminar.grid(row=7, column=1)

btn_consultar = tk.Button(frame, text="Consultar", command=consultar_alumnos)
btn_consultar.grid(row=8, columnspan=2, pady=5)

# Tabla de resultados
tree = ttk.Treeview(root, columns=("Matricula", "Nombre", "Correo"), show="headings")
tree.heading("Matricula", text="Matrícula")
tree.heading("Nombre", text="Nombre")
tree.heading("Correo", text="Correo")
tree.pack(pady=10)

root.mainloop()
