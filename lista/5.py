def imc(x):
    imc = peso/(x*x)
    return imc

x= float (input("Informe sua altura: "))
peso = int (input("Informe seu peso em KG: "))

if imc(x) < 18.5:
    print("Seu imc é classificado como: Abaixo do peso")
elif imc(x) <= 18.5 and imc(x) >= 24.9:
    print("Seu imc é classificado como: Peso normal")
elif imc(x) < 18.5:
    print("Seu imc é classificado como: Abaixo do peso")
elif imc(x) < 18.5:
    print("Seu imc é classificado como: Abaixo do peso")
elif imc(x) < 18.5:
    print("Seu imc é classificado como: Abaixo do peso")