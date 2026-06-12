from InquirerPy import prompt
from rich.panel import Panel
from time import sleep
from rich import print
import random


def strg(text):
    print(f"\n[red]{text:^35}[/]\n")


users = {}


class User:
    def __init__(self, username, password, agency, account, cpf):
        self.username = username
        self.password = password
        self.agency = agency
        self.account = account
        self.balance = 0
        self.cpf = cpf
        self.pix_keys = []

    def cadastro(self):
        strg(" Realize seu Cadastro Kimi ")
        strg(" Gerando agencia... ")
        sleep(0.2)

        self.agency = random.randint(1000, 9999)
        print(self.agency)

        self.username = input("[green]Username:[/] ").strip()

        try:
            self.password = int(input("[red]Password:[/] "))
        except ValueError:
            print("Digite apenas números")

    def login(self, tentativas=0, limite=3):
        while tentativas < limite:
            strg(" Realize seu Login Kimi ")

            username_dg = input("[green]Username:[/] ").strip()

            try:
                password_dg = int(input("[red]Password:[/] "))
            except ValueError:
                print("Senha deve ser número")
                continue

            if username_dg == self.username and password_dg == self.password:
                print(f"\nBem vindo de volta [blue]{self.username}[/]")
                return True
            else:
                print("Nome ou senha incorretos")
                tentativas += 1

        print("Limite de tentativas excedido")
        exit()


class Kimi(User):
    def __init__(self, username, password, agency, account, cpf):
        super().__init__(username, password, agency, account, cpf)

    def painel(self):
        conteudo = f"Agencia: [red]{self.agency}[/]\nSaldo: {self.balance}"
        painel = Panel(conteudo, title=f"Username: <{self.username}>", width=60)
        print(painel)

    def menu(self):
        self.painel()

        menu_kimi = [
            {
                "type": "list",
                "name": "opcao",
                "message": "Selecione uma opção:",
                "choices": [
                    "Deposito",
                    "Saque",
                    "Pix",
                    "Solana",
                    "Sair"
                ]
            }
        ]

        result = prompt(menu_kimi)
        kimi = result["opcao"]
        
        if kimi == "Deposito":
            try:
                amount = float(input("Valor do Depósito: "))
                if amount > 0:
                    self.balance += amount
                    print(f"Depósito de {amount:.2f} realizado com sucesso!")
            except ValueError:
                print("Valor inválido")

        elif kimi == "Saque":
            try:
                amount = float(input("Valor do saque: "))
                if 0 < amount <= self.balance:
                    self.balance -= amount
                    print("Saque realizado!")
                else:
                    print("Saldo insuficiente ou valor inválido")
            except ValueError:
                print("Valor inválido")

        elif kimi == "Pix":
            try:
                dest = input("Destino: ").strip()
                amount = float(input("Valor do Pix: "))

                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Pix de {amount:.2f} enviado para {dest}")
                else:
                    print("Saldo insuficiente")

            except ValueError:
                print("Erro no Pix")

        elif kimi == "Solana":
            saldo_sol = 0
            valor_sol = 500

            painel = Panel(
                f"Sol: {saldo_sol}",
                title="Carteira Solana",
                width=50
            )
            print(painel)

            sol_menu = [
                {
                    "type": "list",
                    "name": "opcao",
                    "message": "Selecione:",
                    "choices": ["Comprar Sol", "Vender Sol", "Sair"]
                }
            ]

            result = prompt(sol_menu)
            opcao = result["opcao"]

            if opcao == "Comprar Sol":
                try:
                    vl = float(input("Quantidade: "))
                    total = vl * valor_sol

                    if total <= self.balance:
                        self.balance -= total
                        saldo_sol += vl
                        print("Compra realizada!")
                    else:
                        print("Saldo insuficiente")
                except ValueError:
                    print("Erro")

            elif opcao == "Vender Sol":
                try:
                    vl = float(input("Quantidade: "))
                    ganho = vl * valor_sol
                    self.balance += ganho
                    print("Venda realizada!")
                except ValueError:
                    print("Erro")

        elif kimi == "Sair":
            strg("Obrigado por testar o sistema")
            sleep(0.5)
            exit()

