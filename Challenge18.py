cars = ['BMW X6', 'BMW i5', 'BMW i8']

user = input('Digite o nome do carro que você deseja comprar: ')

if user in cars:
    print('Este carro está disponível')
else: 
    print('Desculpe este carro não está disponível')