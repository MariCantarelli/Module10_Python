n = int(input('Digite o numero: '))

par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Impar'

print(f'O número {n} é {par_ou_impar(n)}.')
 