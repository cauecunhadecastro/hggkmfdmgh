from random import randint

np = randint (0,100)

while True:
    num_player = int(input("coloca sua tentativa: "))
    if num_player == np:
        print("acertou!")
        break
    elif num_player > np:
        print("pensei um numero menor que esse")
    else:
        print("pensei um numero maior que esse")