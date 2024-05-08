# PyBankExpress v.2.0 Otimizado

**Desafio DIO, projeto "Otimizando o Sistema Bancário com Funções Python"**

## Descrição do Programa

Este programa Python consiste em:

### Funções Principais:

- **menu():** Apresenta um menu de opções para o usuário e retorna a opção escolhida.
- **depositar():** Permite ao usuário depositar dinheiro em sua conta, atualizando o saldo e o extrato da conta.
- **sacar():** Permite ao usuário sacar dinheiro de sua conta, desde que o saldo e os limites permitam, atualizando o saldo, o extrato e o número de saques realizados.
- **exibir_extrato():** Exibe o extrato da conta bancária do usuário, mostrando as transações realizadas e o saldo atual.
- **criar_usuario():** Permite ao usuário criar um novo perfil de usuário, fornecendo informações como nome, CPF, data de nascimento e endereço.
- **filtrar_usuarios():** Filtra a lista de usuários com base no CPF fornecido.
- **criar_conta():** Permite ao usuário criar uma nova conta bancária associada ao seu perfil de usuário existente, fornecendo uma agência e número de conta.
- **listar_contas():** Lista todas as contas bancárias criadas no sistema, exibindo informações como agência, número da conta, nome do titular, CPF e endereço.

### Loop Principal:

Um loop `while` que continua executando até que o usuário escolha a opção de sair (`q`).

### Dados Armazenados:

- Informações dos usuários, como nome, CPF, data de nascimento e endereço, são armazenadas em uma lista.
- As contas bancárias são armazenadas em outra lista, contendo informações como agência, número da conta e o perfil do usuário associado.

### Funcionalidades Adicionais:

- O código inclui verificações de validação para garantir que as operações de depósito e saque estejam dentro dos limites permitidos (saldo, limite e número de saques).
- A exibição do extrato mostra uma mensagem adequada quando não há transações.

Em resumo, a versão 2.0 é uma melhoria de um sistema bancário simples, oferecendo mais funcionalidades e melhorias de usabilidade em comparação com a versão anterior.
