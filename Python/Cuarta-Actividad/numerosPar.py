numeroInicial = 2
numeroFinal = 8
numeroImpares = []

for i in range(numeroInicial,numeroFinal):
    if i % 2 != 0:
        numeroImpares.append(i)

print(numeroImpares)
