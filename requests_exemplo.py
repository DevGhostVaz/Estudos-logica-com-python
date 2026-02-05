# Arquivo: api/requests_exemplo.py
# Exemplo de uso da biblioteca requests para consumir uma API

import requests

def consultar_api_github():
    url = "https://api.github.com"
    try:
        resposta = requests.get(url, timeout=5)

        # Verificando se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            print("Conexão bem-sucedida com a API do GitHub!")
            dados = resposta.json()
            print("Dados recebidos:")
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
        else:
            print(f"Erro na requisição. Código de status: {resposta.status_code}")

    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro ao acessar a API:", e)


def consultar_usuario_github(usuario):
    url = f"https://api.github.com/users/{usuario}"
    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()
            print(f"\nInformações do usuário '{usuario}':")
            print(f"Nome: {dados.get('name', 'Não informado')}")
            print(f"Bio: {dados.get('bio', 'Não informado')}")
            print(f"Repositórios públicos: {dados.get('public_repos', 0)}")
            print(f"Seguidores: {dados.get('followers', 0)}")
            print(f"Seguindo: {dados.get('following', 0)}")
        else:
            print(f"Usuário '{usuario}' não encontrado. Código: {resposta.status_code}")

    except requests.exceptions.RequestException as e:
        print("Erro ao consultar usuário:", e)


def main():
    print("=== Exemplo de consumo de API com requests ===")
    consultar_api_github()

    # Consultando informações de um usuário específico
    consultar_usuario_github("torvalds")  # Linus Torvalds, criador do Linux
    consultar_usuario_github("octocat")   # Usuário exemplo do GitHub


if __name__ == "__main__":
    main()
