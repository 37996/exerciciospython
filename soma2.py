a = int(input("Digite um valor:"))
b = int(input("Digite outro valor:"))
result = a + b
print("A soma entre {} e {} é igual a {}".format(a, b, result))
print ("O próximo numero é {} e o anterior é {}".format(result + 1, result - 1))
print("O dobro de {} é {} e o triplo é {} e a raiz quadrada é {}".format(result, result * 2, result * 3, result ** (1/2)))
print("A média entre {} e {} é {}".format(a, b, result/2))
print("A medida em metros é {}m em Km é {}km".format(result, result / 1000))
print("A tabuada de {} é:\n {} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}\n ".format(result, result, result * 1, result, result * 2, result, result * 3,result, result * 4, result, result * 5, result, result * 6, result, result * 7, result, result * 8, result, result * 9, result, result * 10))
print("Convertendo R${:.2f} para Euro, temos: {:.2f}E".format(result, result / 4.5))