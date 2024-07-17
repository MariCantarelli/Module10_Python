def pot(base, expo = 2):
   return base ** expo

b = int(input("Digite sua base: "))
e = (input('Digite o expoente (default 2): '))

if e: 
    print(f'A potência do número é {pot(b,int(e))}')
else:
    print(f'O resultado é : {pot(b)}')