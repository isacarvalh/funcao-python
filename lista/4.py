def media (x):
    media= s/x
    return media

s=0
x=3

for i in range (1):
    n1= float (input("Informe a nota: "))
    n2= float (input("Informe a nota: "))
    n3= float (input("Informe a nota: "))
    s=n1+n2+n3
    faltas= int (input("Informe a quantidade de faltas: "))
    
    if faltas < 30 and media(x) == 8:
        print(f"O aluno está: aprovado com sucesso com a média: {media(x):.2f}")
    elif faltas >= 30 and media(x) == 8:
        print(f"O aluno está: Reprovado por falta com a média: {media(x):.2f}")
    elif faltas < 30 and media(x) >= 6 and 8:
        print(f"O aluno está: Aprovado com a média: {media(x):.2f}")
    elif faltas >= 30 and media(x) >= 6 and 8:
        print(f"O aluno está: Reprovado por falta com a média: {media(x):.2f}")
    elif faltas < 30 and media(x) == 3 and 5.9:
        print(f"O aluno está: Reprovado com a média: {media(x):.2f}")
    elif faltas >= 30 and media(x) == 3 and 5.9:
        print(f"O aluno está: Reprovado por falta com a média: {media(x):.2f}")
    elif faltas < 30 and media(x) < 3:
        print(f"O aluno está: Reprovado com a média: {media(x):.2f} ")
    elif faltas >= 30 and media(x) < 3:
        print(f"O aluno está: Reprovado por falta com a média: {media(x):.2f} ")
    elif faltas >= 30 and media(x) == 0:
        print(f"O aluno está: Reprovado por falta com a média: {media(x):.2f} ")
    elif faltas < 30 and media(x) == 0:
        print(f"O aluno está: Reprovado com a média: {media(x):.2f} ")