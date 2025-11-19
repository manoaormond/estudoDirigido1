# Função 1 (base)
def saudacao(nome):
    return f"Olá, {nome}!"

# Função 2 (tarefa)
def idade_para_100(idade):
    if idade >= 100:
        return 0
    return 100 - idade

# Código Principal
usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))

print(saudacao(usuario))

anos_restantes = idade_para_100(idade_usuario)
print(f"Faltam {anos_restantes} anos para você completar 100 anos.")