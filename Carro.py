# Arquivo: poo/carro.py
# Exemplo de Programação Orientada a Objetos (POO) em Python

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} foi ligado.")
        else:
            print(f"O carro {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.modelo} foi desligado.")
        else:
            print(f"O carro {self.modelo} já está desligado.")

    def acelerar(self):
        if self.ligado:
            print(f"O carro {self.modelo} está acelerando!")
        else:
            print(f"Não é possível acelerar, o carro {self.modelo} está desligado.")

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Status: {'Ligado' if self.ligado else 'Desligado'}")


# Exemplo de uso da classe Carro
def main():
    carro1 = Carro("Fusca", 1975, "Azul")
    carro1.exibir_informacoes()
    carro1.ligar()
    carro1.acelerar()
    carro1.desligar()

    print("\n--- Outro carro ---")
    carro2 = Carro("Gol", 2020, "Prata")
    carro2.exibir_informacoes()
    carro2.ligar()
    carro2.acelerar()


if __name__ == "__main__":
    main()
