# Arquivo: arquivos/manipulacao.py
# Exemplo de manipulação de arquivos em Python

def escrever_arquivo(nome_arquivo, conteudo):
    """Cria ou sobrescreve um arquivo com o conteúdo fornecido."""
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")


def adicionar_conteudo(nome_arquivo, conteudo):
    """Adiciona conteúdo ao final de um arquivo existente."""
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write("\n" + conteudo)
    print(f"Conteúdo adicionado ao arquivo '{nome_arquivo}'.")


def ler_arquivo(nome_arquivo):
    """Lê e exibe o conteúdo de um arquivo."""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            print(f"\nConteúdo do arquivo '{nome_arquivo}':")
            print(f.read())
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")


def main():
    nome = "exemplo.txt"

    # Criando e escrevendo no arquivo
    escrever_arquivo(nome, "Este é o primeiro conteúdo do arquivo.")

    # Adicionando mais conteúdo
    adicionar_conteudo(nome, "Esta é uma nova linha adicionada.")

    # Lendo o arquivo
    ler_arquivo(nome)


if __name__ == "__main__":
    main()
