def es_primo(numero: int) -> bool:
    for i in range(2, numero):
        if(numero % i == 0):
            return False

    return True

def main():
    numero : int = int(input("Ingresar un número: "))

    if(es_primo(numero)):
        print("El número " + str(numero) + " es primo")
        return

    print("El número " + str(numero) + " no es primo")

main()