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
        return "Erro! Divisão por zero."

def calculadora():
    print("Escolha uma operação:")
    print("a. Soma")
    print("b. Subtração")
    print("c. Multiplicação")
    print("d. Divisão")
    
    operacao = input("Digite o número da operação (a/b/c/d): ")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == 'a':
        print(f"Resultado: {soma(num1, num2)}")
    elif operacao == 'b':
        print(f"Resultado: {subtracao(num1, num2)}")
    elif operacao == 'c':
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == 'd':
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Operação inválida!")

calculadora()