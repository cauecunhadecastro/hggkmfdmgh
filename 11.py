nr_inicial = int(input("numero inicial:"))
nr_final = int(input("numero final:"))
soma = 0
escolha = int(input("escolhe 1 pra ver impar, escolhe 2 pra par"))

if escolha == 1:
    for num in range(nr_inicial, nr_final):
        if num % 2 == 1:
            print(num, end=" ")
            soma = soma + num

if escolha == 2:
    for num in range(nr_inicial, nr_final):
        if num % 2 == 0:
            print(num, end=" ")
            soma = soma + num


print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print(F"a soma dos números no ecrã é{soma}")s