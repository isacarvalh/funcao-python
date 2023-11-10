def dobro(x): # definindo a função - nome(parametro, parametro, ...)
    dobro = x*2 # definir o que ela executa
    return dobro # o que ela retorna

x = int (input("Informe um número: "))

print(dobro(x)) # chamando a função - nome_da_funcao (parametro)


# uma função que calcula o quadrado de um número

def quadrado(x):
    quadrado = x**2
    return quadrado 

x= int (input("Informe x: "))
print(f"O quadrado de {x} é: {quadrado(x)}")