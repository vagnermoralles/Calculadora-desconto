# Programa para cálculo de descontos progressivos

#Entrada das informações
nome = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da compra: "))

#Processamento (Escolha adeqquada da porcentagem a ser aplicada)
if valor_compra < 200.00:
    desconto_percentual = 5
elif valor_compra < 300.00:
    desconto_percentual = 10
else:
    desconto_percentual = 15

#Cálculo do desconto
valor_desconto = valor_compra * (desconto_percentual / 100)
valor_final = valor_compra - valor_desconto

# Saída 
print(f"Obrigado pela preferência, {nome}!")
print(f"Como sua compra teve valor total de: R$ {valor_compra:.2f}")
print(f"\nDesconto aplicado ({desconto_percentual}%): R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
