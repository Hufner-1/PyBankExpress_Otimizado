import textwrap

def menu():
    menu = """\n
    --------=MENU=---------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [Nu]\tNovo Usuario
    [q]\tSair
    => """ 
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print("\n@@@@@ Depósito realizado com sucesso! @@@@@")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("@@@ Operação falhou! O valor do saque excede o saldo. @@@")
        return saldo, extrato
    elif excedeu_limite:
        print("@@@ Operação falhou! O valor do saque excede o limite. @@@")
        return saldo, extrato
    elif excedeu_saques:
        print("@@@ Operação falhou! Você excedeu o limite de saques. @@@")
        return saldo, extrato
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n@@@@@ Saque realizado com sucesso! @@@@")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n------------= EXTRATO =------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=------------------------------------=")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print(f"Usuário já cadastrado com o CPF {usuario['cpf']}.")
        return 
    nome = input("Informe o nome completo:  ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):  ")
    endereco = input("Informe o endereço (logradouro, nrm - bairro - cidade/sigla estado):  ")

    usuarios.append({"nome" : nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n@@@ Conta criada com sucesso! @@@")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas: 
        linha = f"""\
            Agência: {conta["agencia"]}
            Número da conta: {conta["numero_conta"]}
            Nome: {conta["usuario"]["nome"]}
            CPF: {conta["usuario"]["cpf"]}
            Endereço: {conta["usuario"]["endereco"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
            print("Usuário criado com sucesso!")

        elif opcao =="nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            numero_conta += 1
            print("Conta criada com sucesso!")

        elif opcao == "lc":
            listar_contas(contas)
            print("Contas listadas com sucesso!")
            print(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
