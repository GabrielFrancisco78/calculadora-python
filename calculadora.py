# Calculadora Simples em Python

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("=== Calculadora Simples ===")
print("Operações disponíveis: +, -, *, /")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Escolha a operação: ")

if op == "+":
    print("Resultado:", soma(a, b))
elif op == "-":
    print("Resultado:", subtracao(a, b))
elif op == "*":
    print("Resultado:", multiplicacao(a, b))
elif op == "/":
    print("Resultado:", divisao(a, b))
else:
    print("Operação inválida!")
