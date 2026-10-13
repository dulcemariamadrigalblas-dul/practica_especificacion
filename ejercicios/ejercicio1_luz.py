''' 
ENUNCIADO DEL PROBLEMA

Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes. 
'''

#PROBLEMA: calcular el importe del recibo a partir del consumo del mes

#ENTRADAS
#nombre_variable: consumo
#tipo: float
#unidad: kWh
#rango valido: consumo >= 0

#SALIDAS
#nombre_variable: recibo
#tipo: float
#unidad: $
#formato en que se mostrara: 2 decimales

#REGLAS Y SUPUESTOS
# - Valores fijos del problema: tarifas de consumo
#- limites exactos de cada condición: 150 kWh y 280 kWh
#- regla del redondeo: redondear a 2 decimales

# ALGORITMO
# 1. leer consumo
#2. si consumo <= 150: recibo = consumo * 1.00
#       resultado = recibo
#3. En caso contrario, si consumo <= 280: recibo = (150 * 1.00) + ((consumo - 150) * 1.50)
#       resultado = recibo
#4. Mostrar recibo = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)


#CASOS DE PRUEBA
# Casos de prueba: 5
# Entrada: n=100, 150, 200, 280, 300
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#calcularPago(consumo: float) -> float
#leerConsumo() -> float
#mostrarRecibo(recibo: float) -> None
#implementa el algoritmo anterior utilizando las funciones del contrato

def calcularPago(consumo: float) -> float:
    if consumo <= 150:
        recibo = consumo * 1.00
    elif consumo <= 280:
        recibo = (150 * 1.00) + ((consumo - 150) * 1.50)
    else:
        recibo = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)
    return round(recibo, 2)

def leerConsumo() -> float:
    consumo = float(input("Ingrese el consumo en kWh: "))
    return consumo

def mostrarRecibo(recibo: float) -> None:
    print(f"El importe del recibo es: ${recibo}")
