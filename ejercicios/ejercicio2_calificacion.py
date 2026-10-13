''' 
ENUNCIADO DEL PROBLEMA

La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó. 
'''

#PROBLEMA: mostrar la calificación final y si el alumno aprobó. 

#ENTRADAS
#nombre_variable: calificaciones
#tipo: list
#unidad: puntos
#rango valido: calificaciones[i] >= 0

#SALIDAS
#nombre_variable: promedio
#tipo: float
#unidad: puntos
#formato en que se mostrara: 2 decimales

# nombre_variable: estado
#tipo: str
#unidad: texto
#formato en que se mostrara: "Aprobado" o "Reprobado"

#REGLAS Y SUPUESTOS
# - Valores fijos del problema: porcentajes de los parciales
#- limites exactos de cada condición: 70 y 50
#- regla del redondeo: redondear a 2 decimales

# ALGORITMO
# 1. leer parciales
#2. calcular promedio
#3. si promedio >= 70: estado = "Aprobado"
#       en caso contrario, si parcial < 50: estado = "Reprobado"
#       en caso contrario: estado = "Aprobado"
#4. Mostrar resultado

#CASOS DE PRUEBA
# Casos de prueba: 4
# Entrada: n= [80, 90, 70], [70, 70, 70], [100, 40, 100], [70, 70, 69]
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerParciales() -> list
#calcularFinal(parciales: list) -> float
#determinarEstado(promedio: float, parciales: list) -> str
#mostrarResultado(promedio: float, estado: str) -> None

def leerParciales() -> list:
    parciales = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota del parcial {i+1}: "))
        parciales.append(nota)
    return parciales

def calcularFinal(parciales: list) -> float:
    return round((parciales[0] * 0.3) + (parciales[1] * 0.3) + (parciales[2] * 0.4), 2)

def determinarEstado(promedio: float, parciales: list) -> str:
    if promedio >= 70:
        return "Aprobado"
    elif any(nota < 50 for nota in parciales):
        return "Reprobado"
    else:
        return "Aprobado"

def mostrarResultado(promedio: float, estado: str) -> None:
    print(f"Calificación final: {promedio}")
    print(f"Estado: {estado}")
