
elementos = input('Introduce paises separados por coma: ')
paises = [pais for pais in elementos.split(",")]
paisesOrdenados=sorted(list(set(paises)))

print(paisesOrdenados)
