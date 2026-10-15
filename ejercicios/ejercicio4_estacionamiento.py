''' 
ENUNCIADO DEL PROBLEMA

Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción.
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y
muestra el importe a cobrar. 

'''

#PROBLEMA: Calcular y mostrar el importe a cobrar por el tiempo de estancia en un estacionamiento, considerando el cobro por hora y el cobro máximo. 

#ENTRADAS
#nombre_variable: minutos
#tipo: int
#unidad: minutos
#rango válido: minutos >= 0 y minutos <= 1440

#SALIDAS
#nombre_variable: cobro
#tipo: float
#unidad: pesos

#nombre_variable: mensaje
#tipo: str
#unidad: texto
#rango válido: "Cobro: $X.XX" o "Tiempo no válido"

#REGLAS Y SUPUESTOS
#-valores fijos del problema: $20 la primera hora, $15 por cada hora adicional o fracción, cobro máximo de $150
#-limites exactos de cada condicion: 0 a 1440 minutos, 0 a 150 pesos
#-regla del redondeo: redondear a dos decimales


#ALGORITMO
#1. Leer el tiempo de estancia en minutos
#2. Validar que el tiempo esté en el rango válido (0 a 1440)
#3. Calcular el cobro según las reglas del problema
#4. Redondear el cobro a dos decimales
#5. Mostrar el mensaje correspondiente

#CASOS DE PRUEBA
# Casos de prueba: 5
# Entrada: n= [45, 60, 61, 150,600] 
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerMinutos() -> int
#calcularCobro(minutos: int) -> float
#mostrarCobroFinal(cobro: float) -> None


def leerMinutos() -> int:
    minutos = int(input("Ingrese el tiempo de estancia en minutos: "))
    return minutos


def calcularCobro(minutos: int) -> float:
    if minutos < 0 or minutos > 1440:
        return -1.0

    if minutos <= 60:
        cobro = 20
    else:
        horas_adicionales = (minutos - 60 + 59) // 60
        cobro = 20 + horas_adicionales * 15

    if cobro > 150:
        cobro = 150
    return round(cobro, 2)

def mostrarCobroFinal(cobro: float) -> None:
    if cobro < 0:
        print("Tiempo no válido")
    else:
        print(f"Cobro: ${cobro:.2f}")



