from functools import reduce

lista = [1,2,3,4,5,6,7]

#calculo de los numeros impares
impares = list(filter(lambda x : x % 2,lista))
print(impares)

#suma de los numeros impares
suma = reduce (lambda a,b : a + b,impares)
print(suma)