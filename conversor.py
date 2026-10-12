"""Conversor de temperatura entre celsius a Fahrenheit. """

def celsiusFahrenheit(num):
    """ Esta funcion convierte de grados celsius a Fahrenheit"""

    res = num * 9/5 + 32

    return res

def fahrenheitCelsius(num):
    """ Esta funcion convierte de grados Fahrenheit a celsius"""
    
    res = (num  - 32) * 5/9

    return res

def main():
    print("Conversor de temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opc = int(input("Elige una opcion (1 o 2): "))
    num = float(input("Introduce la temperatura: "))

    if (opc == 1):
        print(f"{num}ºC = {celsiusFahrenheit(num)}ºF")
        
    elif (opc ==2):
        print(f"{num}ºF = {fahrenheitCelsius(num)}ºC")
    else:
        print("La opcion no es válida")

if __name__=="__main__":
    main()