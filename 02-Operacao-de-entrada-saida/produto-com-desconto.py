# Entrada de dados básicos

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto em porcentagem: "))

# Processamento computacional

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# Saída da informação

print(f"Preço informado: R$ {preco:.2f}")
print(f"Desconto informado: R$ {desconto:.1f}%")
print(f"Valor d desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {preco_final:.2f}")