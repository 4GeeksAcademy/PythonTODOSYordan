import csv
import os

# Lista global en memoria para almacenar las tareas
todos = []

def load_todos():
    """Carga las tareas desde el archivo todos.csv hacia la memoria."""
    global todos
    todos = []
    if os.path.exists("todos.csv"):
        try:
            with open("todos.csv", mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Evitar líneas vacías
                        todos.append(row[0])
            print("Tareas cargadas exitosamente desde todos.csv.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
    else:
        print("No se encontró un archivo todos.csv previo. Iniciando con lista vacía.")

def save_todos():
    """Guarda las tareas actuales en todos.csv con un formato reutilizable."""
    try:
        with open("todos.csv", mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            for task in todos:
                writer.writerow([task])
        print("Tareas guardadas exitosamente en todos.csv.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def add_one_task(title):
    """Agrega correctamente nuevas tareas a la lista activa."""
    if title.strip():
        todos.append(title.strip())
        print(f"Tarea agregada: '{title.strip()}'")
    else:
        print("El título de la tarea no puede estar vacío.")

def print_list():
    """Muestra las tareas en orden con posiciones que el usuario pueda referenciar."""
    if not todos:
        print("\nNo hay tareas pendientes en la lista.")
    else:
        print("\n--- LISTA DE TAREAS ---")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")
        print("-" * 23)

def delete_task(number_to_delete):
    """Elimina la tarea correcta usando su posición y actualiza bien la lista resultante."""
    try:
        index = int(number_to_delete) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f"Tarea eliminada: '{removed}'")
        else:
            print("Número de tarea fuera de rango.")
    except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    # Cargar tareas al iniciar la aplicación
    load_todos()
    
    while True:
        print("\n=== GESTOR DE TAREAS CLI ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Guardar tareas")
        print("5. Cargar tareas")
        print("6. Salir")
        
        choice = input("\nElige una opción (1-6): ").strip()
        
        if choice == "1":
            print_list()
        elif choice == "2":
            title = input("Escribe el título de la nueva tarea: ")
            add_one_task(title)
        elif choice == "3":
            print_list()
            if todos:
                num = input("Ingresa el número de la tarea que deseas eliminar: ")
                delete_task(num)
        elif choice == "4":
            save_todos()
        elif choice == "5":
            load_todos()
        elif choice == "6":
            # Guardado automático al salir por seguridad operativa
            save_todos()
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 1 y 6.")

if __name__ == "__main__":
    main()