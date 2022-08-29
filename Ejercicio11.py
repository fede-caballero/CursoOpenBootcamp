
def num_primo():
    num = int(input("Ingresa un numero entero: "))

    if num > 1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                print("El numero ingresado (" ,num, ") no es un numero primo ")
                break
        else:
            print("El numero ingresado (", num, ") es un numero primo")
    else:
        print("El numero ingresado debe ser mayor a 1")

print(num_primo())
