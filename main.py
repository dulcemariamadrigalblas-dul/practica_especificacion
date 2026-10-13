from ejercicios.ejercicio1_luz import leerConsumo, calcularPago, mostrarRecibo
from ejercicios.ejercicio2_calificacion import leerParciales, calcularFinal, determinarEstado, mostrarResultado
from ejercicios.ejercicio3_compra import leerSubtotal, calcularDescuento, calcularIVA, calcularTotal, mostrarTicket


def main():
    while True:
        print("Seleccione una opción:")
        print("1. Calcular recibo de luz")
        print("2. Calcular calificación final")
        print("3. Calcular ticket de compra")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            calcularReciboLuz()
        elif opcion == "2":
            parciales = leerParciales()
            promedio = calcularFinal(parciales)
            estado = determinarEstado(promedio, parciales)
            mostrarResultado(promedio, estado)
        elif opcion == "3":
            subtotal = leerSubtotal()
            descuento = calcularDescuento(subtotal)
            iva = calcularIVA(subtotal, descuento)
            total = calcularTotal(subtotal, descuento, iva)
            mostrarTicket(subtotal, descuento, iva, total)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
    consumo = leerConsumo()
    recibo = calcularPago(consumo)
    mostrarRecibo(recibo)

   
if __name__ == "__main__":
    main()

