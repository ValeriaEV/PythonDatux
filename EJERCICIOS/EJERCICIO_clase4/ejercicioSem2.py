#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir. 


def saludar():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo electrónico: ")
    return {"nombre": nombre, "edad": edad, "correo": correo, "cursos": []}

def realizar_operacion():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = "Operación no válida"
    print("El resultado de la operación es:", resultado)

def agregar_a_lista(lista_alumnos):
    alumno = {}
    alumno["nombre"] = input("Ingrese su nombre: ")
    alumno["edad"] = input("Ingrese su edad: ")
    alumno["correo"] = input("Ingrese su correo electrónico: ")
    alumno["cursos"] = []

    while True:
        curso_nombre = input("Ingrese el nombre del curso (o escriba 'fin' para terminar): ")
        if curso_nombre.lower() == 'fin':
            break
        curso_notas = input("Ingrese las notas del curso separadas por coma: ").split(',')
        cursos_alumno = {"nombre_curso": curso_nombre, "notas": [float(nota) for nota in curso_notas]}
        alumno["cursos"].append(cursos_alumno)

    lista_alumnos.append(alumno)

def calcular_promedio_notas(lista_alumnos):
    notas_finales = []
    for alumno in lista_alumnos:
        promedio_alumno = 0
        total_notas = 0
        for curso in alumno["cursos"]:
            total_notas += sum(curso["notas"])
        if total_notas != 0:
            promedio_alumno = total_notas / sum(len(curso["notas"]) for curso in alumno["cursos"])
        notas_finales.append(promedio_alumno)
    return notas_finales

def mostrar_aprobados(lista_alumnos):
    print("Listado de alumnos aprobados:")
    for alumno in lista_alumnos:
        promedio = sum(sum(curso["notas"]) / len(curso["notas"]) for curso in alumno["cursos"]) / len(alumno["cursos"])
        if promedio >= 11:
            print(f"{alumno['nombre']} (Promedio: {promedio:.2f})")

def mostrar_desaprobados(lista_alumnos):
    print("Listado de alumnos desaprobados:")
    for alumno in lista_alumnos:
        promedio = sum(sum(curso["notas"]) / len(curso["notas"]) for curso in alumno["cursos"]) / len(alumno["cursos"])
        if promedio < 11:
            print(f"{alumno['nombre']} (Promedio: {promedio:.2f})")

def generar_lista_multiplos():
    limite_superior = 10**10
    step = 1  # Definimos el step como 1 para revisar cada número en el rango
    lista_multiplos = [num for num in range(1, limite_superior + 1, step) if num % 2 == 0 and num % 5 == 0 and num % 7 == 0]
    print("Tamaño de la lista de múltiplos:", len(lista_multiplos))

def obtener_mayor():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return max(num1, num2)

def menu():
    lista_alumnos = []
    while True:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Realizar operación matemática")
        print("3. Agregar a lista de alumnos")
        print("4. Calcular promedio de notas y agregar notas finales a una lista")
        print("5. Mostrar listado de alumnos aprobados")
        print("6. Mostrar listado de alumnos desaprobados")
        print("7. Generar lista de múltiplos")
        print("8. Obtener el mayor de 2 números")
        print("9. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            agregar_a_lista(lista_alumnos)
        elif opcion == '2':
            realizar_operacion()
        elif opcion == '3':
            agregar_a_lista(lista_alumnos)
        elif opcion == '4':
            # Calcular promedio de notas y agregar notas finales a una lista
            notas_finales = calcular_promedio_notas(lista_alumnos)
            print("Promedio de notas de cada alumno:")
            for i, promedio in enumerate(notas_finales):
                print(f"Alumno {i+1}: {promedio:.2f}")
        elif opcion == '5':
            mostrar_aprobados(lista_alumnos)
        elif opcion == '6':
            mostrar_desaprobados(lista_alumnos)
        elif opcion == '7':
            generar_lista_multiplos()
        elif opcion == '8':
            mayor = obtener_mayor()
            print("El mayor número es:", mayor)
        elif opcion == '9':
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 9.")

menu()