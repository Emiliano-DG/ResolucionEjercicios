f = open ('archivo.txt','w')
f.write('Hola mundo\n')
f.close()

#Escribo por segunda vez
f = open('archivo.txt', 'a')
f.write('hello world')
f.close()