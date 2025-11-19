senha_correta = "python123"
tentativa = ""
max_tentativas = 3
tentativas_usadas = 0

while tentativa != senha_correta and tentativas_usadas < max_tentativas:
    tentativa = input(f"Tentativa {tentativas_usadas + 1}/{max_tentativas}. Digite a senha: ")

    if tentativa == senha_correta:
        print("Acesso liberado!")
    else:
        tentativas_usadas += 1
        if tentativas_usadas < max_tentativas:
            print("Senha incorreta. Tente novamente.")
        else:
            print("Acesso bloqueado! Você excedeu 3 tentativas.")