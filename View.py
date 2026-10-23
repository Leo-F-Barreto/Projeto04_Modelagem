from Model import BancoDados
from Controller import ContaController


class BancoView:
    def __init__(self):
        self.db = BancoDados()
        self.controller = ContaController(view=self, banco_dados=self.db)

    def obter_dados_cliente(self):
        """Método de leitura da View."""
        print("\n--- CADASTRO DE CLIENTE ---")
        nome = input("Digite o Nome do titular: ").strip()
        cpf = input("Digite o CPF do titular: ").strip()

        while True:
            try:
                saldo_inicial = float(input("Digite o Saldo Inicial (R$): "))
                if saldo_inicial < 0:
                    print("O saldo inicial não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

        return nome, cpf, saldo_inicial

    def exibir_conta_criada(self, conta):
        """Exibe os dados da conta recém-criada."""
        print("\n" + "=" * 40)
        print(f"{'CONTA CRIADA COM SUCESSO':^40}")
        print("=" * 40)
        print(f"Número da Conta : {conta.numero}")
        print(f"Titular          : {conta.titular.nome}")
        print(f"CPF do Titular   : {conta.titular.cpf}")
        print(f"Saldo Inicial    : R$ {conta.saldo:.2f}")
        print("=" * 40 + "\n")

    def exibir_lista_contas(self, contas):
        """Exibe todas as contas existentes formatadas na tela."""
        print("\n" + "=" * 55)
        print(f"{'LISTA DE CONTAS EXISTENTES':^55}")
        print("=" * 55)
        print(f"{'CONTA':<7} | {'TITULAR':<25} | {'SALDO':<15}")
        print("-" * 55)
        for conta in contas:
            print(f"{conta.numero:<7} | {conta.titular.nome:<25} | R$ {conta.saldo:>12.2f}")
        print("=" * 55 + "\n")

    def exibir_mensagem_erro(self, mensagem):
        """Exibe avisos ou erros formatados."""
        print(f"\n⚠️  [Aviso]: {mensagem}\n")

    def executar_interface(self):
        """Loop principal do menu no terminal."""
        while True:
            print("=== SISTEMA BANCÁRIO ===")
            print("1. Cadastrar Nova Conta")
            print("2. Visualizar Contas Existentes")
            print("3. Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.controller.cadastrar_nova_conta()
            elif opcao == "2":
                self.controller.listar_contas()
            elif opcao == "3":
                print("\nEncerrando o sistema. Até logo!")
                break
            else:
                print("\nOpção inválida!\n")


if __name__ == "__main__":
    app = BancoView()
    app.executar_interface()