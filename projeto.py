import random

print("Bem-vindo, este jogo é sobre adivinhar um numero")
print("Estou pensando em um número de 1 a 100.")

numero_aleatorio = random.randint(1, 100)
tentativas = 0

while True:
    resposta = input("Digite sua resposta (ou 'sair' para encerrar): ")
    if resposta.lower() == 'sair':
        print("Jogo encerrado. O número era:", numero_aleatorio)
        break
    if not resposta.isdigit():
        print("Por favor, digite um número válido!")
        continue

    resposta = int(resposta)
    tentativas += 1

    if resposta < numero_aleatorio:
        print("Muito baixo! Tente novamente.")
    elif resposta > numero_aleatorio:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! conseguiste acertar em {tentativas} tentativas.")
        break


