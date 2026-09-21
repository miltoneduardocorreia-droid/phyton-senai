# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados básicos

nome_produto = (input("Digite o nome do produto: "))
preco_produto = float(input("Digite o preço do produto: "))
qtd_produto = float(input("Digite a quantidade comprada: "))


# Processamento computacional

valor_final = preco_produto * qtd_produto

# Saída da informação

print(f"Digite o nome do produto: {nome_produto}")
print(f"Digite o preço do produto: R$ {preco_produto:.2f}")
print(f"Digite a quantidade comprada: {qtd_produto}")
print(f"Valor final: R$ {valor_final:.2f}")