def dobro (n):
    return n * 2 

def quadrado(n):
    return n ** 2
num = int(input('Digite um numero: '))

resposta = quadrado(dobro(num))
print(f'A resposta é {resposta}.')
