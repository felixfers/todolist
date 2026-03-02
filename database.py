import sqlite3

def inicializar_db():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas 
                      (id INTEGER PRIMARY KEY, 
                       nombre TEXT NOT NULL, 
                       descripcion TEXT, 
                       estado TEXT DEFAULT 'pendiente')''')
    conn.commit()
    conn.close()

def agregar_tarea(nombre, descripcion):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (nombre, descripcion) VALUES (?, ?)", (nombre, descripcion))
    conn.commit()
    conn.close()

def obtener_pendientes():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, descripcion FROM tareas WHERE estado = 'pendiente'")
    tareas = cursor.fetchall()
    conn.close()
    return tareas