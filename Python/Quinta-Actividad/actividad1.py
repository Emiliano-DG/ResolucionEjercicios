import math

def areaTriangulo(altura,base):
    return (altura*base)/2


def areaCirculo(radio):
    return (math.pi*(radio**2))

areaTriangulo = areaTriangulo(2,8)
areaCirculo = areaCirculo(1)

print('El area del triangulo es: ',areaTriangulo)
print('El area del circulo es: ',areaCirculo)
