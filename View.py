from Model import Cliente, Conta, BancoDados


def obter_dados_cliente():
    """Método de entrada isolado para ler e validar os dados do usuário."""
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


def executar_interface():
    """Interface principal que gerencia o fluxo do terminal."""
    db = BancoDados()
    contador = 1

    while True:
        print("=== SISTEMA BANCÁRIO ===")
        print("1. Cadastrar Nova Conta")
        print("2. Imprimir Dados de uma Conta")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            # Chama o método isolado de leitura de dados
            nome, cpf, saldo_inicial = obter_dados_cliente()

            # Geração automática do número da conta
            numero_conta = f"{contador:03d}"

            # Instanciação dos objetos usando os dados lidos
            cliente = Cliente(nome, cpf)
            conta = Conta(numero_conta, cliente, saldo_inicial)

            # Salva no banco de dados simulado
            db.salvar_conta(conta)
            print(f"\nConta cadastrada com sucesso! Número: {numero_conta}")
            contador += 1

        elif opcao == "2":
            numero_busca = input("\nDigite o número da conta (ex: 001): ").strip()
            conta_encontrada = db.buscar_conta_por_numero(numero_busca)

            if conta_encontrada:
                # Chama o método de impressão formatada da própria conta
                conta_encontrada.imprimir_dados()
            else:
                print("Conta não encontrada!\n")

        elif opcao == "3":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida!\n")


if __name__ == "__main__":
    executar_interface()