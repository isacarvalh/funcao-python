print("CALCULADORA!")
print()
print("Adição: +")
print("Subtração: -")
print("Multiplicação: *")
print("Divisão: /")
print()

l_soma = []
l_sub = []
l_mult = []
l_div = []

choice = input("Deseja fazer uma operação? [ s ou n ]: ")

if choice == 's':
    op = input("Qual operacao (+, -, *, /): ")
    if op == '+':
        def soma(a, b):
            soma = a+b
            return soma
        a = float(input("Digite o a: "))
        b = float(input("Digite o b: "))
        print(f"Resultado: {a} + {b} = ", soma(a, b))
        l_soma.append(soma(a, b))

choice = input("Deseja fazer uma operação? [ s ou n ]: ")

if choice == 's':
    op = input("Qual operacao (+, -, *, /): ")
    if op == '-':
        def subtracao(a, b):
            subtracao= a-b
            return subtracao
    a = float(input("Digite o a: "))
    b = float(input("Digite o b: "))
    print(f"Resultado: {a} - {b} = ", subtracao(a, b))
    l_sub.append(subtracao(a, b))

choice = input("Deseja fazer uma operação? [ s ou n ]: ")

if choice == 's':
    op = input("Qual operacao (+, -, *, /): ")
    if op == '*':
        def multiplicacao(a, b):
            multiplicacao = a*b
            return multiplicacao
    a = float(input("Digite o a: "))
    b = float(input("Digite o b: "))
    print(f"Resultado: {a} x {b} = ", multiplicacao(a, b))
    l_mult.append(multiplicacao(a, b))

choice = input("Deseja fazer uma operação? [ s ou n ]: ")

if choice == 's':
    op = input("Qual operacao (+, -, *, /): ")
    if op == '/':
        def divisao(a, b):
            divisao = a/b
            return divisao
    a = float(input("Digite o a: "))
    b = float(input("Digite o b: "))
    print(f"Resultado: {a} / {b} = ", divisao(a, b))
    l_div.append(divisao(a, b))

elif choice == 'n':
    print("Calculadora desligada!")

print()
print("Histórico de resultados: ")
print("Adições efetuadas:", l_soma)
print("Subtrações efetuadas:", l_sub)
print("Multiplicações efetuadas:", l_mult)
print("Divisões efetuadas:", l_div)
