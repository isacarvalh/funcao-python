choice = input("Deseja fazer uma operação? [ s ou n ]: ")

if choice == 's':
  op = input("Qual operacao (+, -, *, /): ")
elif op == '+':
    def soma (a):
        soma = a+b 
        return soma
    a = float (input("Digite o a: "))
    b = float (input("Digite o b: "))
    print("Resultado: ", soma(a))
    choice = input("Deseja fazer uma operação? [ s ou n ]: ")
    if choice == 's':
     op = input("Qual operacao (+, -, *, /): ")
     if op == '-':
      def subtracao (a):
        subtracao = a-b 
        return subtracao
    a = float (input("Digite o a: "))
    b = float (input("Digite o b: "))
    print("Resultado: ", subtracao(a))
    choice = input("Deseja fazer uma operação? [ s ou n ]: ")
    if choice == 's':
     op = input("Qual operacao (+, -, *, /): ")
    elif op == '*':
      def multiplicacao (a):
        multiplicacao = a*b 
        return multiplicacao
    a = float (input("Digite o a: "))
    b = float (input("Digite o b: "))
    print("Resultado: ", multiplicacao(a))

