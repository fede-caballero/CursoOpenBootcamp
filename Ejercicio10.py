from math import pi

def tria(b, h):
    return b * h/2

bt = float(input("Defina la base del triangulo: "))
ht = float(input("Defina la altura del triangulo: "))

print("El area del triangulo es: ",tria(bt, ht), "cm^2")

def circ(r):
    return pi * r**2

rc = float(input("Defina el radio del circulo: "))
area = circ(rc)
print(f"El radio del circulo es:  {area:.2f} cm^2")
