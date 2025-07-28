# wifi_meter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
import sqlite3
import datetime
import threading
import time

DB_PATH = "InternetSpeed.db"

#Función para crear tabla en la base de datos
def crear_tabla():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            ping REAL,
            download REAL,
            upload REAL
        )
    ''')
    conn.commit()
    conn.close()

# Función para guardar resultado
def guardar_resultado(ping, download, upload):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resultados (fecha, ping, download, upload) VALUES (?, ?, ?, ?)", 
                   (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ping, download, upload))
    conn.commit()
    conn.close()

# Función para mostrar últimos registros
def mostrar_registros():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados ORDER BY id DESC LIMIT 10")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Función para probar velocidad con hilo
def medir_en_hilo():
    btn_probar.config(state="disabled")
    hilo = threading.Thread(target=probar_velocidad)
    hilo.start()

# Función principal de medición
def probar_velocidad():
    try:
        progress_ping['value'] = 0
        progress_download['value'] = 0
        progress_upload['value'] = 0
        lbl_resultado.config(text="⏳ Midiendo...")

        s = speedtest.Speedtest(secure=True)
        s.get_best_server()

        # Ping
        ping = s.results.ping
        progress_ping['value'] = min(ping, 100)

        # Download
        download = round(s.download() / 1_000_000, 2)
        progress_download['value'] = min(download, 100)

        # Upload
        upload = round(s.upload() / 1_000_000, 2)
        progress_upload['value'] = min(upload, 100)

        # Mostrar resultados
        lbl_resultado.config(text=f"✅ Ping: {ping:.2f} ms | ↓ {download} Mbps | ↑ {upload} Mbps")
        guardar_resultado(ping, download, upload)
        mostrar_registros()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
    finally:
        btn_probar.config(state="normal")

# INTERFAZ GRÁFICA
ventana = tk.Tk()
ventana.title("Medidor de Velocidad de Internet")
ventana.geometry("600x400")

notebook = ttk.Notebook(ventana)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="📶 Medir Velocidad")
notebook.add(tab2, text="📋 Ver Registros")
notebook.pack(expand=True, fill="both")

# TAB 1 - MEDICIÓN
btn_probar = tk.Button(tab1, text="Probar Velocidad", command=medir_en_hilo, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_probar.pack(pady=10)

progress_ping = ttk.Progressbar(tab1, length=400, mode='determinate', maximum=100)
progress_ping.pack(pady=5)
tk.Label(tab1, text="Ping").pack()

progress_download = ttk.Progressbar(tab1, length=400, mode='determinate', maximum=100)
progress_download.pack(pady=5)
tk.Label(tab1, text="Velocidad de Descarga").pack()

progress_upload = ttk.Progressbar(tab1, length=400, mode='determinate', maximum=100)
progress_upload.pack(pady=5)
tk.Label(tab1, text="Velocidad de Subida").pack()

lbl_resultado = tk.Label(tab1, text="", font=("Arial", 10))
lbl_resultado.pack(pady=10)

# TAB 2 - REGISTROS
tree = ttk.Treeview(tab2, columns=("ID", "Fecha", "Ping", "Download", "Upload"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)
tree.pack(expand=True, fill="both", padx=10, pady=10)

crear_tabla()
mostrar_registros()
ventana.mainloop()