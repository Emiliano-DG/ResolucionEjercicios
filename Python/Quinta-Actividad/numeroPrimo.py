


def esPrimo(num):
    if num == 1:
        return False
    else:
        contador = 0    
    for i in range(1 , num+1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


num = int(input('Ingrese un numero: '))

if esPrimo(num):
    print('Es primo')
else:
    print('No es primo')