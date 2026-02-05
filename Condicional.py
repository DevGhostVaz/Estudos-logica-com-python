# Exemplo de Condicional em Python

def verificar_idade(idade):
    if idade < 0:
        print("Erro: idade inválida!")
    elif idade < 12:
        print("Você é uma criança.")
    elif idade < 18:
        print("Você é um adolescente.")
    elif idade < 60:
        print("Você é um adulto.")
    else:
        print("Você é um idoso.")

def main():
    try:
        idade = int(input("Digite sua idade: "))
        verificar_idade(idade)
    except ValueError:
        print("Erro: você deve digitar um número inteiro.")

if __name__ == "__main__":
    main()
