def fatorial(n):
    if n == 0 or n ==1:
        return 1 
    else:
        return n * fatorial(n - 1)
    
input = int(input('Digite o número: '))
print(f'O fatorial de {input} é {fatorial(input)}')