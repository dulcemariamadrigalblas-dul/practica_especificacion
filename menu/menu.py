
from ejercicios import ejercicio5_renta as ej5
from ejercicios import ejercicio6_cine as ej6

# 2. La función que llama al contrato
def ejecutarEjercicio5():
 horas = ej5.leerHoras()
 importe = ej5.calcularRenta(horas)
 ej5.mostrarRenta(horas, importe)

def ejecutarEjercicio6():
 edad = ej6.leerEdad()
 cobro = ej6.calcularPrecio(edad: int) -> float
 ej6.mostrarPrecio(edad, cobro)



# 3. En mostrarMenu y en menus, la opción nueva
print("5. Renta de bicicletas")
print("6.Cine")

...
elif opcion == "5":
 ejecutarEjercicio5()

elif opcion == "6":
 ejecutarEjercicio6()

