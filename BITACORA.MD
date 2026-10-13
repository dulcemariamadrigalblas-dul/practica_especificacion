Ej.1 CASO 1. EJERCICIO 1 calcular el importe del recibo a partir del consumo del mes
ENTRADA
 100      200        280        300    
ESPERADO (A MANO)
$100      $225.0     $345.0     $405.0
OBTENIDO
$100       $225.0    $345.0     $405.0
COINCIDE
SI           SI        SI         SI

Ej1: código generado con Copilot
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Ingrese el consumo en kWh: 100
El importe del recibo es: $100.0
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Ingrese el consumo en kWh: 150
El importe del recibo es: $150.0
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Ingrese el consumo en kWh: 200
El importe del recibo es: $225.0
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Ingrese el consumo en kWh: 280
El importe del recibo es: $345.0
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Ingrese el consumo en kWh: 300
El importe del recibo es: $405.0



Ej.2 CASO 1. EJERCICIO 2 mostrar la calificación final y si el alumno aprobó
ENTRADA
 80,70,90          70,70,70           100,100,40          69,70,70    
ESPERADO (A MANO)
81.0 (Aprobado)     70.0 (Aprobado)    76.0 (Aprobado)     69.7 (Aprobado)
OBTENIDO
81.0 (Aprobado)     70.0 (Aprobado)     76.0 (Aprobado)    69.7 (Aprobado)
COINCIDE
  SI                      SI                  SI                 SI

Ej1: código generado con Copilot
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Salir
Ingrese el número de la opción deseada: 2
Ingrese la nota del parcial 1: 80
Ingrese la nota del parcial 2: 70
Ingrese la nota del parcial 3: 90
Calificación final: 81.0
Estado: Aprobado
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Salir
Ingrese el número de la opción deseada: 2
Ingrese la nota del parcial 1: 70
Ingrese la nota del parcial 2: 70
Ingrese la nota del parcial 3: 70
Calificación final: 70.0
Estado: Aprobado
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Salir
Ingrese el número de la opción deseada: 2  
Ingrese la nota del parcial 1: 100
Ingrese la nota del parcial 2: 100
Ingrese la nota del parcial 3: 40
Calificación final: 76.0
Estado: Aprobado
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Salir
Ingrese el número de la opción deseada: 2
Ingrese la nota del parcial 1: 69
Ingrese la nota del parcial 2: 70
Ingrese la nota del parcial 3: 70
Calificación final: 69.7
Estado: Aprobado
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Salir
Ingrese el número de la opción deseada: 3
Saliendo del programa.


Ej.3 CASO 1. EJERCICIO 3 calcular el ticket
ENTRADA
 500                     900                     1000                          5000    
ESPERADO (A MANO)        
$500.00, 0, 80, 580     900, 0, 144, 1044       1000, 100, 144, 1044          5000,1000,640,4640
OBTENIDO
$500.00, 0, 80, 580     900, 0, 144, 1044       1000, 100, 144, 1044           5000,1000,640,4640
COINCIDE
SI                                SI                   SI                          SI

Ej3: código generado con Copilot
PS C:\Users\197112-5\Downloads\practica_especificacion> python .\main.py
Seleccione una opción:
1. Calcular recibo de luz
2. Calcular calificación final
3. Calcular ticket de compra
4. Salir
Ingrese el número de la opción deseada: 3
Ingrese el subtotal: 500
----- TICKET -----
Subtotal: $500.00
Descuento: $0.00
IVA: $80.00
Total: $580.00
------------------
Seleccione una opción:
1. Calcular recibo de luz
2. Calcular calificación final
3. Calcular ticket de compra
4. Salir
Ingrese el número de la opción deseada: 3
Ingrese el subtotal: 900
----- TICKET -----
Subtotal: $900.00
Descuento: $0.00
IVA: $144.00
Total: $1044.00
------------------
Seleccione una opción:
1. Calcular recibo de luz
2. Calcular calificación final
3. Calcular ticket de compra
4. Salir
Ingrese el número de la opción deseada: 3
Ingrese el subtotal: 1000
----- TICKET -----
Subtotal: $1000.00
Descuento: $100.00
IVA: $144.00
Total: $1044.00
------------------
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Calcular ticket de compra
4.Salir
Ingrese el número de la opción deseada: 3
Ingrese el subtotal: 5000
----- TICKET -----
Subtotal: $5000.00
Descuento: $1000.00
IVA: $640.00
Total: $4640.00
------------------
Seleccione una opción:
1.Calcular recibo de luz
2.Calcular calificación final
3.Calcular ticket de compra
4.Salir