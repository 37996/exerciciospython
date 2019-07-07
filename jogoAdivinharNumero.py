from random import randint
n = int(randint(1, 20))
p = 0
t = 0
while p != n:
    p = int(input("Insira o seu palpite: "))
    t += 1
    if p == n:
        print("Acertou! Em {} tentativas ".format(t))
    elif p < n:
        print("Chute um valor maior")
    else:
        print("Chute um valor menor")
print("Fim do jogo.")
