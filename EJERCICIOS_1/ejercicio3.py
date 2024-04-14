# 3. Realice un programa que calcule la suma de los numeros hasta el valor ingresado.
# Ejemplo : Si ingresa 5 se tendra que calcular 1+2+3+4+5
numero= int(input("Ingrese un numero: "))
suma = sum(range(1, numero + 1))
print("La suma de los números hasta", numero, "es:", suma)