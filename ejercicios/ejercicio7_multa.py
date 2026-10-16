''' 
ENUNCIADO DEL PROBLEMA

En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa es de $500. Si se excede
por más de 20 km/h, la multa es de $1,000. Se necesita mostrar la multa a partir de la velocidad del
vehículo.

'''

#PROBLEMA: Se necesita mostrar la multa a partir de la velocidad del vehículo

#ENTRADAS
#nombre_variable: velocidad
#tipo: float
#unidad: km/h
#rango valido: velocidad >= 0

#SALIDAS
#nombre_variable: multa
#tipo: float
#unidad: $
#formato en que se mostrara: 2 decimales

#REGLAS Y SUPUESTOS
# - Valores fijos del problema: límite de 60 km/h; multas de $500 y $1,000
#- limites exactos de cada condición: velocidad <= 60 km/h: $0; 60 < velocidad <= 80 km/h: $500; velocidad > 80 km/h: $1,000
#- regla del redondeo: redondear a 2 decimales

# ALGORITMO
# 1. leer velocidad
#2. si velocidad <= 60: multa = 0
#3. En caso contrario: si velocidad <= 80, multa = 500; si no, multa = 1000
#4. Mostrar multa
 


#CASOS DE PRUEBA
# Casos de prueba: 5
# Entrada: n=50, 60, 61, 80, 81
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerVelocidad() -> float
#calcularMulta(velocidad: float) -> float
#mostrarMulta(multa: float) -> None

def leerVelocidad() -> float:
    velocidad = float(input("Ingrese la velocidad en km/h: "))
    return velocidad

def calcularMulta(velocidad: float) -> float:
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000
    return round(multa, 2)

def mostrarMulta(multa: float) -> None:
    print(f"Multa: ${multa:.2f}") 