class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    


class Coche(Vehiculo):
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad=velocidad
        self.cilindrada = cilindrada

    def __str__(self):
         return f'color {self.color},ruedas {self.ruedas} ,puertas {self.puertas},velocidad {self.velocidad}, cilindrada {self.cilindrada}'

coche = Coche('Rojo',4,4,130,1400)
print(coche)