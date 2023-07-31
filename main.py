import sys


account = {
    "name": "Usuário",
    "balance": 1000,
}


def main():
    print("Bem-vindo ao sistema bancário")
    print("O que você gostaria de fazer?")
    print("1. Depositar dinheiro")
    print("2. Sacar dinheiro")
    print("3. Consultar saldo")
    print("4. Sair")

    choice = input("Escolha uma opção: ")

    while choice != "4":
        if choice == "1":
            amount = int(input("Qual o valor do depósito? "))
            account["balance"] += amount
            print("O saldo da conta é de", account["balance"])
        elif choice == "2":
            amount = int(input("Qual o valor do saque? "))
            if account["balance"] < amount:
                print("Saldo insuficiente")
            else:
                account["balance"] -= amount
                print("O saldo da conta é de", account["balance"])
        elif choice == "3":
            print("O saldo da conta é de", account["balance"])
        elif choice == "4":
            print("Saindo...")
            sys.exit(0)
        else:
            print("Opção inválida")

        choice = input("Escolha uma opção: ")


main()
