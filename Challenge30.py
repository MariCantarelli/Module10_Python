n1 = int(input("Digite o 1 número: "))
n2 = int(input("Digite o 2 número:"))

multi = lambda num1, num2: num1 * num2

print(f'A multiplição de {n1} e {n2} é {multi(n1, n2)}.')