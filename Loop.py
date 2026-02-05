# Exemplos de Loop em Python

def loop_for():
    print("=== Exemplo de loop FOR ===")
    # Percorrendo uma lista
    frutas = ["maçã", "banana", "laranja"]
    for fruta in frutas:
        print("Eu gosto de", fruta)

    # Usando range()
    for i in range(5):
        print("Número:", i)


def loop_while():
    print("\n=== Exemplo de loop WHILE ===")
    contador = 0
    while contador < 5:
        print("Contador:", contador)
        contador += 1


def main():
    loop_for()
    loop_while()


if __name__ == "__main__":
    main()
