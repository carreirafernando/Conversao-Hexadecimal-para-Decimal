def verificacao():
    if i == 'a':
        return 10
    elif i == 'b':
        return 11
    elif i == 'c':
        return 12
    elif i == 'd':
        return 13
    elif i == 'e':
        return 14
    elif i == 'f':
        return 15


hex = input('Digite a numeração Hexadecimal: ')
lista = []
for i in hex:
    if i in '0123456789':
        lista.append(int(i))
    else:
        num = verificacao()
        lista.append(num)

total = 0
potencia = len(lista)
for i in lista:
    potencia -= 1
    total += i * (16 ** potencia)
print(f'O número Hexadecimal "{hex}" convertido para Decimal fica: {total}')
