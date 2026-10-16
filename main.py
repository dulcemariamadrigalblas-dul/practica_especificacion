from ejercicios.ejercicio1_luz import leerConsumo, calcularPago, mostrarRecibo
from ejercicios.ejercicio2_calificacion import leerParciales, calcularFinal, determinarEstado, mostrarResultado
from ejercicios.ejercicio3_compra import leerSubtotal, calcularDescuento, calcularIVA, calcularTotal, mostrarTicket
from ejercicios.ejercicio4_estacionamiento import leerMinutos, calcularCobro, mostrarCobroFinal
from ejercicios.ejercicio5_renta import leerHoras, calcularRenta, mostrarRenta
from ejercicios.ejercicio6_cine import leerEdad, calcularPrecio, mostrarPrecio
from ejercicios.ejercicio7_multa import leerVelocidad, calcularMulta, mostrarMulta




def main():
    while True:
        print("Seleccione una opción:")
        print("1. Calcular recibo de luz")
        print("2. Calcular calificación final")
        print("3. Calcular ticket de compra")
        print("4. Calcular cobro de estacionamiento")
        print("5. Calcular renta de equipo")
        print("6. Calcular precio de boleto de cine")
        print("7. Calcular Multa")
        print("8. Salir")
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
            minutos = leerMinutos()
            cobro = calcularCobro(minutos)
            mostrarCobroFinal(cobro)
        elif opcion == "5": 
            horas = leerHoras()
            importe = calcularRenta(horas)
            mostrarRenta(importe)
        elif opcion == "6":
            edad = leerEdad()
            precio = calcularPrecio(edad)
            mostrarPrecio(precio)
        elif opcion == "7":
            velocidad = leerVelocidad()
            multa = calcularMulta(velocidad)
            mostrarMulta(multa)
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
   
if __name__ == "__main__":
    main()


