# Crie uma lista com algumas linguagens de programação.
# Crie uma cópia dessa lista usando copy().
# Use um "for" ou "while" para mostrar as linguagens da lista copiada.
# Lista de linguagens
linguagens = ["Python", "JavaScript", "Java", "PHP"]
copia_seguranca = linguagens.copy()
print(linguagens)
print(copia_seguranca)
for linguagem in copia_seguranca:
    print('-', linguagem)