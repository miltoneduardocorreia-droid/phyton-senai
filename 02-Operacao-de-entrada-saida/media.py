# Entradas de dados básicos
nome = input("Insira o seu nome: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

# Processamento computacional
media = (n1 + n2) / 2

# Saída das informações
print(f"Aluno: {nome}")

# Formatação com uma casa decimal
# f => significa número de ponto flutuante (decimal)
# .1 => significa mostrar uma casa depois da vírgula
print(f"Média final: {media: .1f}")