age = int(input('Digite sua idade: '))

if age < 13:
   print('Você é uma criança.')
elif age >= 13 and age <= 19:
    print('Você é um adolecente.')
else:
    print('Você é um adulto.')