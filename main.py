from ejercicios.ejercicio1_luz import leerConsumo, calcularPago, mostrarRecibo

def main():
    consumo = leerConsumo()
    recibo = calcularPago(consumo)
    mostrarRecibo(recibo)
if __name__ == "__main__":
    main()

