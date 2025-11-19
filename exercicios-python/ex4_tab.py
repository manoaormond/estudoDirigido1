print("--- Tabuada Completa (1 a 10) ---")

# Laço externo: passa por cada número de 1 a 10
for numero in range(1, 11):
    print(f"\nTabuada do {numero}:")

    # Laço interno: calcula a tabuada daquele 'numero'
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")