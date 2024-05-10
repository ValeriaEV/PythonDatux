from servicios.functions import *
from monitoreo.logger import Logger

log = Logger()

def showOptions():
    msg = """
    Bienvenido al Sistema de Gestión de Ventas:
    1. Cargar datos
    2. Generar reporte de ventas totales
    3. Generar gráfico de las últimas ventas por mes o categoría
    4. Generar bitácora
    5. Salir
    """
    print(msg)
    opcion = int(input("Ingrese la opción: "))
    return opcion

def getFunction(opcion):
    if opcion == 1:
        archivo_cargado = loadData()
        log.message(f'Se realizó la carga del archivo {archivo_cargado}')
    elif opcion == 2:
        generateReport()
        log.message('Se generó el reporte de ventas totales')
    elif opcion == 3:
        showData()
        log.message('Se generó el gráfico de las últimas ventas')
    elif opcion == 4:
        log.showLog()
    elif opcion == 5:
        log.close()
        print("¡Hasta luego!")
        exit()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    while True:
        opcion = showOptions()
        getFunction(opcion)