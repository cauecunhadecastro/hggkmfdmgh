from random import radint
nmr = radint(1, 20)
count = 0
while True:
    count = count + 1
    guess = int(input("Tentativa: "))
    if guess == nmr:
        print("Acertou!!")
        break
    elif guess > nmr:
        print("O numero gerado é MENOR")
    else:
        print("o numero gerado é MAIOR")

print(f"Foram precisas {count} tentativas")