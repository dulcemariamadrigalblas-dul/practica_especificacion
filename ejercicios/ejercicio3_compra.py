''' 
ENUNCIADO DEL PROBLEMA

Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total. 
'''

#PROBLEMA: mostrar el ticket con subtotal, descuento, IVA y total. 

#ENTRADAS
#nombre_variable: subtotal
#tipo: float
#unidad: pesos
#rango valido: subtotal >= 0

#SALIDAS
#nombre_variable: descuento
#tipo: float
#unidad: pesos
#formato en que se mostrara: 2 decimales

# nombre_variable: iva
#tipo: float
#unidad: pesos
#formato en que se mostrara: 2 decimales

# nombre_variable: total
#tipo: float
#unidad: pesos
#formato en que se mostrara: 2 decimales


#REGLAS Y SUPUESTOS
# - Valores fijos del problema: porcentajes de descuento y de IVA
#- limites exactos de cada condición: $1,000 y $5,000
#- regla del redondeo: redondear a 2 decimales

# ALGORITMO
# 1. leer subtotal
#2. calcular descuento
#3. calcular iva
#4. calcular total
#5. Mostrar ticket

#CASOS DE PRUEBA
# Casos de prueba: 4
# Entrada: n= [$500], [$900], [$1,000], [$5,000]
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerSubtotal() -> float
#calcularDescuento(subtotal: float) -> float
#calcularIVA(subtotal: float, descuento: float) -> float
#calcularTotal(subtotal: float, descuento: float, iva: float) -> float
#mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None

def leerSubtotal() -> float:
    subtotal = float(input("Ingrese el subtotal: "))
    return subtotal

def calcularDescuento(subtotal: float) -> float:
    if subtotal >= 5000:
        return subtotal * 0.2
    elif subtotal >= 1000:
        return subtotal * 0.1
    return 0

def calcularIVA(subtotal: float, descuento: float) -> float:
    return (subtotal - descuento) * 0.16

def calcularTotal(subtotal: float, descuento: float, iva: float) -> float:
    return subtotal - descuento + iva

def mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None:
    print("----- TICKET -----")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
    print("------------------")