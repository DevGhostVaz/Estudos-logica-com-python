# Exemplo de uso de Dicionário em Python

def main():
    # Criando um dicionário
    pessoa = {
        "nome": "João",
        "idade": 25,
        "cidade": "São Paulo"
    }

    # Exibindo o dicionário completo
    print("Dicionário pessoa:", pessoa)

    # Acessando valores pelas chaves
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Cidade:", pessoa["cidade"])

    # Adicionando nova chave/valor
    pessoa["profissao"] = "Desenvolvedor"
    print("Após adicionar profissão:", pessoa)

    # Alterando valores
    pessoa["idade"] = 26
    print("Após atualizar idade:", pessoa)

    # Removendo uma chave
    del pessoa["cidade"]
    print("Após remover cidade:", pessoa)

    # Iterando sobre as chaves e valores
    print("\nIterando sobre o dicionário:")
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")

    # Verificando se uma chave existe
    if "nome" in pessoa:
        print("\nA chave 'nome' existe no dicionário!")

    # Usando get() para evitar erro se a chave não existir
    sobrenome = pessoa.get("sobrenome", "Não informado")
    print("Sobrenome:", sobrenome)


if __name__ == "__main__":
    main()
