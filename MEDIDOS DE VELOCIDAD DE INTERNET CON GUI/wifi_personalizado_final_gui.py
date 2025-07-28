import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
import sqlite3
import datetime
import threading
import time

DB_PATH = "InternetSpeed.db"

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

def guardar_resultado(ping, download, upload):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resultados (fecha, ping, download, upload) VALUES (?, ?, ?, ?)", 
                   (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ping, download, upload))
    conn.commit()
    conn.close()

def mostrar_registros():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados ORDER BY id DESC LIMIT 10")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

def medir_en_hilo():
    btn_probar.config(state="disabled")
    hilo = threading.Thread(target=probar_velocidad)
    hilo.start()

def probar_velocidad():
    try:
        progress_ping['value'] = 0
        progress_download['value'] = 0
        progress_upload['value'] = 0
        lbl_resultado.config(text="⏳ Midiendo...")

        s = speedtest.Speedtest(secure=True)
        s.get_best_server()

        ping = s.results.ping
        progress_ping['value'] = min(ping, 100)

        download = round(s.download() / 1_000_000, 2)
        progress_download['value'] = min(download, 100)

        upload = round(s.upload() / 1_000_000, 2)
        progress_upload['value'] = min(upload, 100)

        lbl_resultado.config(text=f"✅ Ping: {ping:.2f} ms | ↓ {download} Mbps | ↑ {upload} Mbps")
        guardar_resultado(ping, download, upload)
        mostrar_registros()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
    finally:
        btn_probar.config(state="normal")

def contar():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def contar_en_hilo():
    hilo = threading.Thread(target=contar)
    hilo.start()

# GUI
ventana = tk.Tk()
ventana.title("Medidor de Velocidad de Internet")
ventana.geometry("600x420")

# Estilos personalizados para las barras
style = ttk.Style()
style.theme_use('default')
style.configure("Ping.Horizontal.TProgressbar", troughcolor='white', background='green')
style.configure("Download.Horizontal.TProgressbar", troughcolor='white', background='blue')
style.configure("Upload.Horizontal.TProgressbar", troughcolor='white', background='orange')

# Pestañas
notebook = ttk.Notebook(ventana)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="📶 Medir Velocidad")
notebook.add(tab2, text="📋 Ver Registros")
notebook.pack(expand=True, fill="both")

# TAB 1 - Medición
btn_probar = tk.Button(tab1, text="Probar Velocidad", command=medir_en_hilo, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_probar.pack(pady=10)

progress_ping = ttk.Progressbar(tab1, length=400, mode='determinate', maximum=100, style="Ping.Horizontal.TProgressbar")
progress_ping.pack(pady=5)
tk.Label(tab1, text="Ping").pack()

progress_download = ttk.Progressbar(tab1, length=400, mode='determinate', maximum=100, style="Download.Horizontal.TProgressbar")
progress_download.pack(pady=5)
tk.Label(tab1, text="Velocidad de Descarga").pack()

progress_upload = ttk.Progressbar(tab1, length=400, mode='determinate', maximum=100, style="Upload.Horizontal.TProgressbar")
progress_upload.pack(pady=5)
tk.Label(tab1, text="Velocidad de Subida").pack()

lbl_resultado = tk.Label(tab1, text="", font=("Arial", 10))
lbl_resultado.pack(pady=10)

btn_contar = tk.Button(tab1, text="Contar en Hilo", command=contar_en_hilo, bg="#2196F3", fg="white")
btn_contar.pack(pady=5)

# TAB 2 - Registros
tree = ttk.Treeview(tab2, columns=("ID", "Fecha", "Ping", "Download", "Upload"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)
tree.pack(expand=True, fill="both", padx=10, pady=10)

crear_tabla()
mostrar_registros()
ventana.mainloop()