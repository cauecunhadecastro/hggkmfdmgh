velocidade = int(input("velocidade:"))

if velocidade  > 80 :
    excesso = velocidade - 80

    multa = excesso * 2
    print(f"foi gerado uma multa de:{multa} ")
else:
    print("dentro do limite")