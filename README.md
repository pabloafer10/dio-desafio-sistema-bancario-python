# 🏦 Projeto Bootcamp DIO - Sistema Bancário

#### Este é um sistema bancário simples desenvolvido em Python, com funcionalidades básicas de operações financeiras, como:

##### ✅ Depósito de valores
##### ✅ Saque de dinheiro
##### ✅ Consulta de Extrato

#### 📌 Regras de Negócio
##### 🔹 Depósitos:

###### * Apenas valores positivos são permitidos.
###### * Em caso de valor inválido deve ser exibido a mensagem: "Valor inválido, tente novamente."
###### * Todos os depósitos devem ser armazenados e exibidos na consulta de extrato.

##### 🔹 Saques:

###### * Limite diário de 3 saques.
###### * Caso o limite diário de saque seja maior do que permitido, deve ser exibido a mensagem: "Limite de saques diário excedido,! Por favor, tente novamente."
###### * Valor máximo de R$ 500,00 por saque.
###### * Caso o saldo seja insuficiente, deve ser exibido a mensagem: "Saldo insuficiente! Por favor, tente novamente." 
###### * Caso o valor do saque seja inválido, deve ser exibido a mensagem: "Valor informado inválido, tente novamente."
###### * Todos os saques devem ser armazenados e exibidos na consulta de extrato.

##### 🔹 Extrato:

###### * Deve listar todos os depósitos e saques realizados.
###### * No final, exibe o saldo disponível no formato: R$ xxx.xx.

##### 🔹 Outras regras:

###### * O usuário pode optar por sair do sistema a qualquer momento.
###### * Se a entrada do usuário for inválida (não estiver no menu de opções), deve ser exibido a mensagem: "Opção inválida, por favor seleciona novamente a operação desejada."

