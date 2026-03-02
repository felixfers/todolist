import database

def menu():
    database.inicializar_db()  # <--- AÑADE ESTA LÍNEA AQUÍ
    #print("--- 📝 AGREGAR NUEVA TAREA ---")

    print("--- 📝 AGREGAR NUEVA TAREA ---")
    nombre = input("Nombre de la tarea: ")
    descripcion = input("Descripción (opcional): ")
    
    if nombre.strip():
        database.agregar_tarea(nombre, descripcion)
        print(f"✅ Tarea '{nombre}' guardada con éxito.")
    else:
        print("⚠️ El nombre no puede estar vacío.")

if __name__ == "__main__":
    menu()
