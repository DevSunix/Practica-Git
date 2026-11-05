estudiantes = []

def registrar_estudiante(nombre, calificacion): 
    # Guardamos cada estudiante como un diccionario
    estudiantes.append({"nombre": nombre, "calificacion": calificacion}) 
    print(f"Estudiante registrado: {nombre} - Calificación: {calificacion}") 

def consultar_estudiantes(): 
    print("\n--- ESTUDIANTES REGISTRADOS ---") 
    for estudiante in estudiantes: 
        print(f"Nombre: {estudiante['nombre']} | Calificación: {estudiante['calificacion']}")

def calcular_promedio():
    if not estudiantes:
        print("\nNo hay estudiantes registrados para calcular el promedio.")
        return 0.0
    
    suma = sum(estudiante["calificacion"] for estudiante in estudiantes)
    promedio = suma / len(estudiantes)
    print(f"\nEl promedio general de las calificaciones es: {promedio:.2f}")
    return promedio


# --- Ejemplo de uso ---
registrar_estudiante("Juan Pérez", 8.5) 
registrar_estudiante("María López", 9.5)
registrar_estudiante("Carlos Gómez", 7.0)

consultar_estudiantes()
calcular_promedio()
