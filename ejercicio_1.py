from math import pi

def area_trinagulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return pi * radio**2

def main():
    base_triangulo = float(input('Ingresar base del triángulo: '))
    altura_trinagulo = float(input('Ingresar altura del triángulo: '))

    print("El área del triángulo es: " + str(area_trinagulo(base_triangulo, altura_trinagulo)))

    radio = float(input("Ingresar el radio del circulo: "))
    print("El área del circulo es: " + str(area_circulo(radio)))

main()
