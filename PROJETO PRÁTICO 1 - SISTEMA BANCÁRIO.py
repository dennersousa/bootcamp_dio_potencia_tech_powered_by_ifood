class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def saque(self, valor):
        if valor > 0 and valor <= 500 and len(self.saques) < 3:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor inválido para saque ou limite diário de saques atingido.")

    def extrato(self):
        print("========= EXTRATO =========:")
        if not self.depositos and not self.saques:
            print("  Não foram realizadas movimentações.")
        else:
            for valor in self.depositos:
                print(f"  Depósito: R$ {valor:.2f}")
            for valor in self.saques:
                print(f"  Saque: R$ {valor:.2f}")
        print(f"  Saldo atual: R$ {self.saldo:.2f}")


def main():
    banco = SistemaBancario()

    while True:
        print("\nMenu:")
        print("[1] Depósitar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            banco.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            banco.saque(valor)
        elif opcao == '3':
            banco.extrato()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
