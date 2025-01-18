from random import randint
from time import sleep

lanc = 0

face = int(input("qual a face do dado?"))

while True:
    dado = randint(1, 100000000000000)
    lanc = lanc + 1
    print(f"saio o número {dado}")
    if dado == face:
        break
    print(f"foram nescessario {lanc} tentativas")