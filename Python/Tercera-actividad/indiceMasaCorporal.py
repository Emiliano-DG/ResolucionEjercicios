import math

peso = float(input('Ingrese su peso '))
altura = float(input('ingrese su altura en metros '))

imc = round(peso/math.pow(altura,2),1)

print('Tu indice de masa corporal es ', imc)
