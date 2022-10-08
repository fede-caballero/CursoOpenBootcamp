def bisiesto():
  anio = int(input("Introduce un año por favor: "))

  if (anio % 4 == 0 and (anio % 400 == 0 or anio % 100 == 0)):
      print(f"El numero introducido {anio} es de un año bisiesto!")
      
  else:
      print(f"El año {anio} introducido no es bisiesto!")

bisiesto()
