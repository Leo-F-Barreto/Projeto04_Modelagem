from Model import Cliente, Conta, BancoDados


class ContaController:
    def __init__(self, view, banco_dados: BancoDados):
        self.view = view
        self.db = banco_dados
        self._contador_contas = 1

    def cadastrar_nova_conta(self):
        """Coordena o fluxo de criação de conta."""
        nome, cpf, saldo_inicial = self.view.obter_dados_cliente()
        numero_conta = f"{self._contador_contas:03d}"

        cliente = Cliente(nome, cpf)
        nova_conta = Conta(numero=numero_conta, cliente=cliente, saldo_inicial=saldo_inicial)

        self.db.salvar_conta(nova_conta)
        self._contador_contas += 1

        self.view.exibir_conta_criada(nova_conta)

    def listar_contas(self):
        """Busca as contas no Model e envia para a View exibir."""
        # Acessa a lista protegida de contas do BancoDados
        lista_de_contas = self.db._contas

        if not lista_de_contas:
            self.view.exibir_mensagem_erro("Nenhuma conta cadastrada no sistema.")
        else:
            self.view.exibir_lista_contas(lista_de_contas)
