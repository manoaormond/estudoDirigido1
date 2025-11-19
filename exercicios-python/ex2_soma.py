num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Soma
resultado_soma = num1 + num2
print(f"A soma é: {resultado_soma}")

# Subtração
resultado_subtracao = num1 - num2
print(f"A subtração é: {resultado_subtracao}")

# Multiplicação
resultado_multiplicacao = num1 * num2
print(f"A multiplicação é: {resultado_multiplicacao}")

# Divisão (Usei float() para garantir divisão decimal, se necessário)
# Na divisão, se usar int(), o resultado será um número inteiro.
resultado_divisao = num1 / num2
print(f"A divisão é: {resultado_divisao}")