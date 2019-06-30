import random
a1 = input("Digite o nome do aluno 1: ")
a2 = input("Digite o nome do aluno 2: ")
a3 = input("Digite o nome do aluno 3: ")
a4 = input("Digite o nome do aluno 4: ")
all = [a1, a2, a3, a4]
a = random.choice(all)
print("O aluno é {} ".format(a))



a1 = str(input("Digite o nome do aluno 1: "))
a2 = str(input("Digite o nome do aluno 2: "))
a3 = str(input("Digite o nome do aluno 3: "))
a4 = str(input("Digite o nome do aluno 4: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem é {} ".format(lista))