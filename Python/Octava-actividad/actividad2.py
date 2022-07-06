import pickle


class Vehiculo:

    def __init__(self,marca,color):
        self.marca = marca
        self.color = color

    def __str__(self):
        return f'la marca del auto es {self.marca} y de color {self.color}'

vehiculo = Vehiculo ('PEUGEOT','GRIS')

#Creo el archivo
f = open ('Vechiculo.txt','wb')
pickle.dump(vehiculo,f)
f.close()

#Lectura del archivo
f = open ('Vechiculo.txt','rb')
peugeot = pickle.load(f)
print(peugeot)
f.close()
