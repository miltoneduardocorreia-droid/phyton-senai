# Solicitação de dados
# Define a senha correta
senha_correta = "1234"
# Solicita a senha ao usuário
senha = input("Digite a senha: ")
# Enquanto a senha estiver errada
while senha != senha_correta:
    # Informa que a senha está incorreta
    print("Senha incorreta")
    # Solicita a senha novsamente
    senha = input("Digite a senha novamente: ")
# Quando a condição indicar falso, a senha está correta
print("Senha correta! Acesso permitido")
