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

def transformacao():
    total = 0
    cont = len(hexadecimal)
    for n in hexadecimal:
        cont -= 1
        total += n * (16 ** cont)
    return total

hex = input('Digite a numeração Hexadecimal: ').strip().lower()
hexadecimal = []
for i in hex:
    if i in '0123456789':
        hexadecimal.append(int(i))
    else:
        num = verificacao()
        hexadecimal.append(num)

print(f'O número Hexadecimal "{hex}" convertido para Decimal fica: {transformacao()}')
