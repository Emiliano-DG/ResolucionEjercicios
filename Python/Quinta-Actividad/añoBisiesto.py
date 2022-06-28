def Bisiesto(dato):
    if dato % 4 == 0:
        if dato % 100 == 0:
            if dato % 400 == 0:
                print('El año es bisiesto')
            else:
             print('El año no es bisiesto')
        else:
             print('El año es bisiesto.')
    else:
        print('El año no es bisiesto.')

dato = int(input('Ingrese el año: '))
Biciesto(dato)
