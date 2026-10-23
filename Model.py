class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


class Conta:
    def __init__(self, numero: str, cliente: Cliente, saldo_inicial: float = 0.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo_inicial

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saldo insuficiente ou valor inválido.")
            return False

    def __str__(self):
        return f"Conta: {self.numero} | Titular: {self.titular.nome} | Saldo: R$ {self.saldo:.2f}"


class BancoDados:
    def __init__(self):
        # Lista simulando o banco de dados
        self._contas = []

    def salvar_conta(self, conta: Conta):
        self._contas.append(conta)
        print(f"Conta {conta.numero} salva com sucesso no banco de dados!")

    def buscar_conta_por_numero(self, numero: str) -> Conta | None:
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None

    def listar_todas_contas(self):
        if not self._contas:
            print("Nenhuma conta cadastrada.")
            return
        print("\n--- Lista de Contas no Banco de Dados ---")
        for conta in self._contas:
            print(conta)


# --- Exemplo de Uso ---
if __name__ == "__main__":
    # 1. Instanciando o Banco de Dados simulado
    db = BancoDados()

    # 2. Criando Clientes
    cliente1 = Cliente("Alice Silva", "123.456.789-00")
    cliente2 = Cliente("Bob Souza", "987.654.321-11")

    # 3. Criando Contas
    conta1 = Conta(numero="001-X", cliente=cliente1, saldo_inicial=500.0)
    conta2 = Conta(numero="002-Y", cliente=cliente2, saldo_inicial=100.0)

    # 4. Salvando no Banco de Dados
    print("--- Cadastrando Contas ---")
    db.salvar_conta(conta1)
    db.salvar_conta(conta2)

    # 5. Listando as contas salvas
    db.listar_todas_contas()

    # 6. Buscando e operando em uma conta específica
    print("\n--- Buscando Conta 001-X ---")
    conta_encontrada = db.buscar_conta_por_numero("001-X")
    if conta_encontrada:
        print(f"Conta encontrada! Saldo atual: R$ {conta_encontrada.saldo:.2f}")
        conta_encontrada.depositar(250.0)
        conta_encontrada.sacar(100.0)

    # 7. Verificando o estado atualizado no banco
    db.listar_todas_contas()
