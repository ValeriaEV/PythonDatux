# 4.Realizar un programa que permita saber si un usario puede obtener un tarjeta de credito
# condiciones : ser mayor de 18 años , un ingreso mensual de 1000 soles mensual.
# si cumple con las 2 condiciones imprimir que tipo de tarjeta puede obtener
# si su ingreso mensual es de 1000 hasta 3000 soles es tarjeta de clasica , mayor a ello tarjeta dorada.

edad=int(input("Ingresar su edad: "))
ingreso=int(input("Ingresar su ingreso: "))
if edad>=18 and ingreso>=1000:
    if ingreso<=3000:
        print("Tarjeta clasica")
    else:
        print("Tarjeta dorada")
else:
    print("No cumple con las condiciones")
