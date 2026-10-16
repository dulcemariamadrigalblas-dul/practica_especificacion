''' 
ENUNCIADO DEL PROBLEMA

Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años o más pagan la mitad.
Se necesita mostrar el precio del boleto según la edad.

'''

#PROBLEMA: Se necesita mostrar el precio del boleto según la edad

#ENTRADAS
#nombre_variable: edad
#tipo: int
#unidad: años
#rango valido: edad >= 0

#SALIDAS
#nombre_variable: precio
#tipo: float
#unidad: $
#formato en que se mostrara: 2 decimales

#REGLAS Y SUPUESTOS
# - Valores fijos del problema: $80 por boleto, 50% de descuento para niños de hasta 12 años y adultos de 60 años o más
#- limites exactos de cada condición: edad >= 0
#- regla del redondeo: redondear a 2 decimales

# ALGORITMO
# 1. leer edad
#2. si edad <= 12 or edad >= 60: precio = 80 * 0.5
#       resultado = precio
#3. En caso contrario: precio = 80
#       resultado = precio
#4. Mostrar precio
 


#CASOS DE PRUEBA
# Casos de prueba: 5
# Entrada: n=8, 12, 13, 59, 60
# Salida: resultado

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerEdad() -> int
#calcularPrecio(edad: int) -> float
#mostrarPrecio(precio: float) -> None

def calcularPrecio(edad: int) -> float:
    if edad <= 12 or edad >= 60:
        precio = 80 * 0.5
    else:
        precio = 80
    return round(precio, 2)

def leerEdad() -> int:
    edad = int(input("Ingrese la edad: "))
    return edad

def mostrarPrecio(precio: float) -> None:
    print(f"Precio del boleto: ${precio:.2f}")  
