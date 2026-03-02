import database
import sqlite3

def mostrar_y_completar():
    tareas = database.obtener_pendientes()
    
    if not tareas:
        print("🎉 ¡No tienes tareas pendientes! Todo al día.")
        return

    print("\n--- ✅ MARCAR TAREA COMO HECHA ---")
    for i, (nombre, desc) in enumerate(tareas, 1):
        print(f"{i}. {nombre} ({desc})")

    try:
        opcion = int(input("\nEscribe el número de la tarea que terminaste: "))
        if 1 <= opcion <= len(tareas):
            tarea_seleccionada = tareas[opcion - 1][0] # Obtenemos el nombre
            
            # Conexión rápida para actualizar el estado
            conn = sqlite3.connect('tareas.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE tareas SET estado = 'completada' WHERE nombre = ?", (tarea_seleccionada,))
            conn.commit()
            conn.close()
            
            print(f"👍 ¡Genial! '{tarea_seleccionada}' marcada como completada.")
        else:
            print("❌ Número no válido.")
    except ValueError:
        print("❌ Por favor, introduce un número.")

if __name__ == "__main__":
    mostrar_y_completar()