''' 
ENUNCIADO DEL PROBLEMA

Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. Se
necesita mostrar el importe a pagar según las horas de renta.

'''

#PROBLEMA: Se necesita mostrar el importe a pagar según las horas de renta

#ENTRADAS
#nombre_variable: horas
#tipo: int
#unidad: horas
#rango valido: horas >= 0

#SALIDAS
#nombre_variable: importe
#tipo: float
#unidad: $
#formato en que se mostrara: 2 decimales

#REGLAS Y SUPUESTOS
# - Valores fijos del problema: $30 por hora, 15% de descuento si se rentan 3 horas o más
#- limites exactos de cada condición: horas >= 0
#- regla del redondeo: redondear a 2 decimales

# ALGORITMO
# 1. leer horas
#2. si horas >= 3: importe = (horas * 30) * 0.85
#       resultado = importe
#3. En caso contrario: importe = horas * 30
#       resultado = importe
#4. Mostrar importe
 


#CASOS DE PRUEBA
# Casos de prueba: 4
# Entrada: n=1, 2, 3, 4
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerHoras() -> int
#calcularRenta(horas: int) -> float
#mostrarRenta(importe: float) -> None

def calcularRenta(horas: int) -> float:
    if horas >= 3:
        importe = (horas * 30) * 0.85
    else:
        importe = horas * 30
    return round(importe, 2)

def leerHoras() -> int:
    horas = int(input("Ingrese las horas de renta: "))
    return horas

def mostrarRenta(importe: float) -> None:
    print(f"Importe a pagar: ${importe:.2f}")

    
