numbers = [1, 2, 3, 4, 5, 6]
quadrado = lambda num: num ** 2

resultado = []
for i in numbers:
    resultado.append(quadrado(i))

print(f'Os quadrados dos numeros {numbers} são {resultado}.')