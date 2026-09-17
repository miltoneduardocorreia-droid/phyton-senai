#Faça um programa que peça o ano de nascimento de uma pessoa
#e calcule a sua idade atual.
#Depois, mostre o ano de nascimento e a idade no terminal.

# Entrada de dados básicos

ano_nascimento = int(input("Digite o ano de nascimetno: "))
ano_atual = int(input("Digite o ano atual: "))


# Processamento computacional

idade_atual = ano_atual - ano_nascimento

# Saída da informação

print(f"Digite o ano de nascimento: {ano_nascimento}")
print(f"Digite o ano atual: {ano_atual}")
print(f"A idade é: {idade_atual} anos")
