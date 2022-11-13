import operaciones

x1 = 5
x2 = 7
suma = operaciones.suma(x1, x2)
resta = operaciones.resta(x1, x2)
mult = operaciones.multip(x1, x2)
divi = operaciones.dividir(x1, x2)

print(f"El resultado de la suma de {x1} y {x2} es {suma}")
print(f"El resultado de la resta de {x1} y {x2} es {resta}")
print(f"El resultado de la mult de {x1} y {x2} es {mult}")
print(f"El resultado de la division de {x1} y {x2} es {divi:.2f}")
