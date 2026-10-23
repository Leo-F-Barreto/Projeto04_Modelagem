# controller.py
from Model import Cliente, Conta, BancoDados


class ContaController:
    def __init__(self, view, banco_dados: BancoDados):
        self.view = view
        self.db = banco_dados
        self._contador_contas = 1  # Controla a geração automática de números

    def cadastrar_nova_conta(self):
        """
        Coordena o fluxo de criação: recebe da View, instancia o Model,
        salva no banco e comanda a View para exibir.
        """
        # 1. Recebe os dados brutos vindos da View
        nome, cpf, saldo_inicial = self.view.obter_dados_cliente()

        # Gera o número sequencial da conta
        numero_conta = f"{self._contador_contas:03d}"

        # 2. Instancia o Cliente (Model)
        cliente = Cliente(nome, cpf)

        # 3. Instancia a Conta (Model)
        nova_conta = Conta(numero=numero_conta, cliente=cliente, saldo_inicial=saldo_inicial)

        # 4. Salva na lista do Banco de Dados (Model)
        self.db.salvar_conta(nova_conta)

        # Incrementa o gerador para a próxima conta
        self._contador_contas += 1

        # 5. Comanda a View para exibir a conta que acabou de ser criada
        self.view.exibir_conta_criada(nova_conta)
