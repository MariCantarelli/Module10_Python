cities = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Australia': 'Camberra' ,
    'Chile' : 'Santiago',
    'Canada' : 'Ottawa'
}

user = input('Digite o nome do país: ')

if user in cities:
    print(f'A capital de {user} é {cities[user]}.')
else: 
    print('Desculpe, não temos informações sobre a capital desse país.')