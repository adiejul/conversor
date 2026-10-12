"""Conversor de temperatura entre celsius a farhenheit. """

def celsiusFarhenheit(num):
    """ Esta funcion convierte de grados celsius a fargenheit"""

    res = num * 9/5 + 32

    return res

def farhenheitCelsius(num):
    """ Esta funcion convierte de grados farhenheit a celsius"""
    
    res = (num  - 32) * 5/9

    return res

def main():
    print("Conversor de temperaturas")
    print("1. Celsius a Farhenheit")
    print("2. Farhenheit a Celsius")
    opc = int(input("Elige una opcion (1 o 2): "))
    num = float(input("Introduce la temperatura: "))

    if (opc == 1):
        print(celsiusFarhenheit(num))
    elif (opc ==2):
        print(farhenheitCelsius(num))
    else:
        print("La opcion no es válida")

if __name__=="__main__":
    main()