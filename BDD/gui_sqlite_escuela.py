import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

DB_NAME = "escuela.db"

# === FUNCIONES BASE DE DATOS ===
def execute_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
    except Exception as e:
        rows, columns = [], []
        messagebox.showerror("Error de SQL", str(e))
    finally:
        conn.close()
    return columns, rows

def show_result(frame, columns, rows):
    for widget in frame.winfo_children():
        widget.destroy()
    style = ttk.Style()
    style.configure("Treeview", rowheight=25)
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    for row in rows:
        tree.insert('', 'end', values=row)
    tree.pack(expand=True, fill='both')

# === FUNCIONES CRUD ALUMNOS ===
def insertar_alumno():
    datos = (entry_mat.get(), entry_nom.get(), entry_edad.get(), entry_sem.get(),
             entry_gen.get(), entry_correo.get(), entry_carrera.get())
    query = "INSERT INTO alumno VALUES (?, ?, ?, ?, ?, ?, ?)"
    try:
        execute_query(query, datos)
        messagebox.showinfo("Éxito", "Alumno insertado correctamente.")
        consultar_alumnos()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_alumno():
    mat = entry_mat.get()
    query = "DELETE FROM alumno WHERE mat_alu = ?"
    try:
        execute_query(query, (mat,))
        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        consultar_alumnos()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def consultar_alumnos():
    for row in crud_tree.get_children():
        crud_tree.delete(row)
    query = "SELECT mat_alu, nom_alu, correo_alu FROM alumno"
    for alumno in fetch_query(query)[1]:
        crud_tree.insert('', 'end', values=alumno)

# === FUNCIONES CONSULTAS PREDEFINIDAS ===
def consulta_alumnos_y_carreras():
    query = "SELECT a.nom_alu AS Alumno, c.nom_c AS Carrera FROM alumno a JOIN carrera c ON a.clave_c1 = c.clave_c"
    cols, rows = fetch_query(query)
    show_result(tab2_frame, cols, rows)

def consulta_profesores_y_materias():
    query = "SELECT p.nom_p AS Profesor, m.nom_m AS Materia FROM mat_pro mp JOIN profesor p ON mp.clave_p2 = p.clave_p JOIN materia m ON mp.clave_m2 = m.clave_m"
    cols, rows = fetch_query(query)
    show_result(tab3_frame, cols, rows)

def consulta_personalizada():
    query = query_text.get("1.0", tk.END).strip()
    if not query.lower().startswith("select"):
        messagebox.showwarning("Advertencia", "Solo se permiten consultas SELECT.")
        return
    cols, rows = fetch_query(query)
    show_result(tab4_frame, cols, rows)

# === FUNCIONES CRUD PROFESOR ===
def insertar_profesor():
    datos = (entry_prof_clave.get(), entry_prof_nom.get(), entry_prof_dir.get(),
             entry_prof_tel.get(), entry_prof_hora.get())
    query = "INSERT INTO profesor VALUES (?, ?, ?, ?, ?)"
    try:
        execute_query(query, datos)
        messagebox.showinfo("Éxito", "Profesor insertado correctamente.")
        consultar_profesores()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def consultar_profesores():
    for row in prof_tree.get_children():
        prof_tree.delete(row)
    query = "SELECT clave_p, nom_p, dir_p, tel_p, hora_p FROM profesor"
    for profe in fetch_query(query)[1]:
        prof_tree.insert('', 'end', values=profe)

# === FUNCIONES CRUD MATERIA ===
def insertar_materia():
    datos = (entry_mat_clave.get(), entry_mat_nom.get(),)
    query = "INSERT INTO materia (clave_m, nom_m) VALUES (?, ?)"
    try:
        execute_query(query, datos)
        messagebox.showinfo("Éxito", "Materia insertada correctamente.")
        consultar_materias()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def consultar_materias():
    for row in mat_tree.get_children():
        mat_tree.delete(row)
    query = "SELECT clave_m, nom_m FROM materia"
    for materia in fetch_query(query)[1]:
        mat_tree.insert('', 'end', values=materia)

# === FUNCIONES CRUD CARRERA ===
def insertar_carrera():
    datos = (entry_car_clave.get(), entry_car_nom.get(),)
    query = "INSERT INTO carrera (clave_c, nom_c) VALUES (?, ?)"
    try:
        execute_query(query, datos)
        messagebox.showinfo("Éxito", "Carrera insertada correctamente.")
        consultar_carreras()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def consultar_carreras():
    for row in car_tree.get_children():
        car_tree.delete(row)
    query = "SELECT clave_c, nom_c FROM carrera"
    for carrera in fetch_query(query)[1]:
        car_tree.insert('', 'end', values=carrera)

# === INTERFAZ GRÁFICA PRINCIPAL ===
root = tk.Tk()
root.title("Sistema de Gestión Escolar")
root.geometry("900x600")
root.configure(bg="#f0f2f5")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook.Tab", padding=[10, 6], font=('Segoe UI', 10))
style.configure("TLabel", font=('Segoe UI', 10))
style.configure("TButton", font=('Segoe UI', 10, 'bold'))

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# === PESTAÑA 1: GESTIÓN DE ALUMNOS ===
tab1 = ttk.Frame(notebook)
form = ttk.Frame(tab1, padding=10)
form.pack()

labels = ["Matrícula", "Nombre", "Edad", "Semestre", "Género", "Correo", "Clave Carrera"]
entries = []
for i, label in enumerate(labels):
    ttk.Label(form, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = ttk.Entry(form, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_mat, entry_nom, entry_edad, entry_sem, entry_gen, entry_correo, entry_carrera = entries

btn_frame = ttk.Frame(form)
btn_frame.grid(row=7, columnspan=2, pady=10)
ttk.Button(btn_frame, text="Insertar", command=insertar_alumno).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Eliminar", command=eliminar_alumno).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Consultar", command=consultar_alumnos).grid(row=0, column=2, padx=5)

crud_tree = ttk.Treeview(tab1, columns=("Matrícula", "Nombre", "Correo"), show="headings", height=10)
for col in ("Matrícula", "Nombre", "Correo"):
    crud_tree.heading(col, text=col)
    crud_tree.column(col, width=200, anchor="center")
crud_tree.pack(expand=True, fill='both', padx=10, pady=10)

notebook.add(tab1, text="Gestión de Alumnos")

# === PESTAÑA 2: ALUMNOS Y CARRERAS ===
tab2 = ttk.Frame(notebook)
tab2_frame = ttk.Frame(tab2, padding=10)
tab2_frame.pack(expand=True, fill='both')
ttk.Button(tab2, text="Mostrar Alumnos y Carreras", command=consulta_alumnos_y_carreras).pack(pady=5)
notebook.add(tab2, text="Alumnos - Carreras")

# === PESTAÑA 3: PROFESORES Y MATERIAS ===
tab3 = ttk.Frame(notebook)
tab3_frame = ttk.Frame(tab3, padding=10)
tab3_frame.pack(expand=True, fill='both')
ttk.Button(tab3, text="Mostrar Profesores y Materias", command=consulta_profesores_y_materias).pack(pady=5)
notebook.add(tab3, text="Profesores - Materias")

# === PESTAÑA 4: CONSULTA LIBRE ===
tab4 = ttk.Frame(notebook)
query_text = tk.Text(tab4, height=5, font=('Consolas', 10))
query_text.pack(fill='x', padx=10, pady=5)
ttk.Button(tab4, text="Ejecutar Consulta", command=consulta_personalizada).pack(pady=5)
tab4_frame = ttk.Frame(tab4, padding=10)
tab4_frame.pack(expand=True, fill='both')
notebook.add(tab4, text="Consulta Personalizada")

# === PESTAÑA 5: GESTIÓN DE PROFESORES ===
tab5 = ttk.Frame(notebook)
form_prof = ttk.Frame(tab5, padding=10)
form_prof.pack()

labels_prof = ["Clave Profesor", "Nombre", "Dirección", "Teléfono", "Hora"]
entries_prof = []
for i, label in enumerate(labels_prof):
    ttk.Label(form_prof, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = ttk.Entry(form_prof, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries_prof.append(entry)

entry_prof_clave, entry_prof_nom, entry_prof_dir, entry_prof_tel, entry_prof_hora = entries_prof

btn_prof_frame = ttk.Frame(form_prof)
btn_prof_frame.grid(row=5, columnspan=2, pady=10)
ttk.Button(btn_prof_frame, text="Insertar", command=insertar_profesor).grid(row=0, column=0, padx=5)
ttk.Button(btn_prof_frame, text="Consultar", command=consultar_profesores).grid(row=0, column=1, padx=5)

prof_tree = ttk.Treeview(tab5, columns=labels_prof, show="headings", height=10)
for col in labels_prof:
    prof_tree.heading(col, text=col)
    prof_tree.column(col, width=150, anchor="center")
prof_tree.pack(expand=True, fill='both', padx=10, pady=10)

notebook.add(tab5, text="Gestión de Profesores")

# === PESTAÑA 6: GESTIÓN DE MATERIAS ===
tab6 = ttk.Frame(notebook)
form_mat = ttk.Frame(tab6, padding=10)
form_mat.pack()

labels_mat = ["Clave Materia", "Nombre Materia"]
entries_mat = []
for i, label in enumerate(labels_mat):
    ttk.Label(form_mat, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = ttk.Entry(form_mat, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries_mat.append(entry)

entry_mat_clave, entry_mat_nom = entries_mat

btn_mat_frame = ttk.Frame(form_mat)
btn_mat_frame.grid(row=2, columnspan=2, pady=10)
ttk.Button(btn_mat_frame, text="Insertar", command=insertar_materia).grid(row=0, column=0, padx=5)
ttk.Button(btn_mat_frame, text="Consultar", command=consultar_materias).grid(row=0, column=1, padx=5)

mat_tree = ttk.Treeview(tab6, columns=labels_mat, show="headings", height=10)
for col in labels_mat:
    mat_tree.heading(col, text=col)
    mat_tree.column(col, width=200, anchor="center")
mat_tree.pack(expand=True, fill='both', padx=10, pady=10)

notebook.add(tab6, text="Gestión de Materias")

# === PESTAÑA 7: GESTIÓN DE CARRERAS ===
tab7 = ttk.Frame(notebook)
form_car = ttk.Frame(tab7, padding=10)
form_car.pack()

labels_car = ["Clave Carrera", "Nombre Carrera"]
entries_car = []
for i, label in enumerate(labels_car):
    ttk.Label(form_car, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = ttk.Entry(form_car, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries_car.append(entry)

entry_car_clave, entry_car_nom = entries_car

btn_car_frame = ttk.Frame(form_car)
btn_car_frame.grid(row=2, columnspan=2, pady=10)
ttk.Button(btn_car_frame, text="Insertar", command=insertar_carrera).grid(row=0, column=0, padx=5)
ttk.Button(btn_car_frame, text="Consultar", command=consultar_carreras).grid(row=0, column=1, padx=5)

car_tree = ttk.Treeview(tab7, columns=labels_car, show="headings", height=10)
for col in labels_car:
    car_tree.heading(col, text=col)
    car_tree.column(col, width=200, anchor="center")
car_tree.pack(expand=True, fill='both', padx=10, pady=10)

notebook.add(tab7, text="Gestión de Carreras")

root.mainloop()
