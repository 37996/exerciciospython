d = int(input('Quantos dias o carro ficou alugado? '))
c = 60 * d
km = int(input('Quantos km o carro rodoou? '))
ct = (km * 0.15) + c
print(" O carro ficou alugado por : {} dias e custou {} + 0,15 por Km que totalizou {}".format(d, c, ct))
