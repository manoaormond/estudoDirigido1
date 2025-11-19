# funcoes.py
def exibir_menu():
    print("\n[1] Cadastrar item [2] Listar itens [0] Sair")

def cadastrar(itens):
    nome = input("Digite o nome do item: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    if nome in itens:
        print("Item já existe.")
        return
    itens.append(nome)
    print("Item cadastrado!")

def listar(itens):
    if not itens:
        print("Nenhum item cadastrado.")
    else:
        for i, nome in enumerate(itens, start=1):
            print(f"{i}. {nome}")
def remover(itens):
    if not itens:
        print("Nenhum item para remover.")
        return

    listar(itens)
    
    try:
        num_remover = int(input("Digite o NÚMERO do item para remover (0 para cancelar): "))
        
        if num_remover == 0:
            print("Operação cancelada.")
            return
        if 1 <= num_remover <= len(itens):
            item_removido = itens.pop(num_remover - 1) 
            print(f"Item '{item_removido}' removido com sucesso!")
        else:
            print("Número inválido.")
            
    except ValueError:
        print("Entrada inválida. Digite um número.")