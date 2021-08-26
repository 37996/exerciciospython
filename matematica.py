import math
import random
import emoji
num = int(input('Digiteum numero: '))
raiz = math.sqrt(num)
print(raiz)

n = random.randint(1, 100)
print('Numero random: ', n)

print(emoji.emojize("Olá, Mundo! :sunglasses:", use_aliases=True))

f = float(input("Digite um numero float para ver seu inteiro:"))
print("{} agora é {} ".format(f, math.trunc(f)))
prnti("--------------------------------")


