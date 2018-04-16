#Conversão de algarismos (1 a 10): arábico para romano/romano para arábico

tipo = int(input('Escolha o tipo de conversão que deseja ser feita -> 1 = Arábico / 2 = Romano: '))

if tipo == 1:
    algarismo = input('Digite o algarismo romano que deve ser convertido: ')
    if algarismo == 'I':
        print('O algarismo arábico é: 1')
    elif algarismo == 'II':
        print('O algarismo arábico é: 2')
    elif algarismo == 'III':
        print('O algarismo arábico é: 3')
    elif algarismo == 'IV':
        print('O algarismo arábico é: 4')
    elif algarismo == 'V':
        print('O algarismo arábico é: 5')
    elif algarismo == 'VI':
        print('O algarismo arábico é: 6')
    elif algarismo == 'VII':
        print('O algarismo arábico é: 7')
    elif algarismo == 'VIII':
        print('O algarismo arábico é: 8')
    elif algarismo == 'IX':
        print('O algarismo arábico é: 9')
    elif algarismo == 'X':
        print('O algarismo arábico é: 10')
elif tipo == 2:
    algarismo = int(input('Digite o algarismo arábico que deve ser convertido: '))
    if algarismo == 1:
        print('O algarismo romano é: I')
    elif algarismo == 2:
        print('O algarismo romano é: II')
    elif algarismo == 3:
        print('O algarismo romano é: III')
    elif algarismo == 4:
        print('O algarismo romano é: IV')
    elif algarismo == 5:
        print('O algarismo romano é: V')
    elif algarismo == 6:
        print('O algarismo romano é: VI')
    elif algarismo == 7:
        print('O algarismo romano é: VII')
    elif algarismo == 8:
        print('O algarismo romano é: VIII')
    elif algarismo == 9:
        print('O algarismo romano é: IX')
    elif algarismo == 10:
        print('O algarismo romano é: X')
else:
    print('O algarismo informado não pode ser convertido.')
            
