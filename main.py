estudiantes = [] 
def registrar_estudiante(nombre): 
    estudiantes.append(nombre) 
    print("Estudiante registrado:", nombre) 
registrar_estudiante("Juan Pérez") 
registrar_estudiante("María López")
print("Lista de estudiantes:") 
for estudiante in estudiantes: 
 print(estudiante) 
