# Exemplo de uso de Lista em Python

def main():
    # Criando uma lista
    frutas = ["maçã", "banana", "laranja"]

    # Exibindo a lista completa
    print("Lista de frutas:", frutas)

    # Acessando elementos pelo índice
    print("Primeira fruta:", frutas[0])
    print("Última fruta:", frutas[-1])

    # Adicionando elementos
    frutas.append("uva")
    print("Após adicionar 'uva':", frutas)

    # Removendo elementos
    frutas.remove("banana")
    print("Após remover 'banana':", frutas)

    # Iterando sobre a lista
    print("Percorrendo a lista:")
    for fruta in frutas:
        print("Eu gosto de", fruta)

    # Verificando se um item está na lista
    if "maçã" in frutas:
        print("A maçã está na lista!")

    # Ordenando a lista
    frutas.sort()
    print("Lista ordenada:", frutas)

    # Lista com diferentes tipos de dados
    misturada = [1, "texto", 3.14, True]
    print("Lista misturada:", misturada)


if __name__ == "__main__":
    main()
