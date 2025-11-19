# main.py
from funcoes import exibir_menu, cadastrar, listar, remover

def main():
    itens = []
    print("=== App de Itens (BFD 2.0) ===")
    
    while True:
        print("\n[1] Cadastrar item [2] Listar itens [3] Remover item [0] Sair")
        
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar(itens)
        elif opcao == "2":
            listar(itens)
        elif opcao == "3":
            remover(itens)
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()