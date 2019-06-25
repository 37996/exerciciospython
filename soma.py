a = int(input("Digite um valor:"))
b = int(input("Digite outro valor:"))
result = a + b
print("A soma entre {} e {} é igual a {}".format(a, b, result))
print ("O próximo numero é {} e o anterior é {}".format(result + 1, result - 1))
print("O dobro de {} é {} e o triplo é {} e a raiz quadrada é {}".format(result, result * 2, result * 3, result ** (1/2)))