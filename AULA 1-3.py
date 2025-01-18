NOTA1 = int(input("qual a nota do seu primeiro teste?"))
NOTA2 = int(input("qual a nota do seu segundo teste?"))

media = (NOTA1 + NOTA2) / 2

if 60 > media:
    print("sua nota está muito baixa, você foi reprovado...")

else:
    print("sua nota está acima do nescessario, você foi aprovado...")