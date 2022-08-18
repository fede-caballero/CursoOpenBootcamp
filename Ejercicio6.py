peso = float(input("Por favor ingrese su peso en kg: "))
estat = float(input("Por favor ingrese su estatura en metros: "))

imc = peso / estat**2

print(f"Tu Indice de Masa Corporal es: {imc:.2f}")
