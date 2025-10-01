# problema: [-12938,2356,1293,298091,38372,18375,28301,-2938,53, -98235, 286356, 08341, 93845]
# detectar el menor y el mayor de todos

# min = 999999
# max = -999999

lista = [-12938,2356,1293,298091,38372,18375,28301,-2938,53, -98235, 286356, 0.8341, 93845]

mins = lista[0]
maxs = lista[0]

for var in lista:
    if(var > maxs):
        maxs = var

    if(var < mins):
        mins = var

print("El valor minimo es:", mins)
print("El valor maximo es:", maxs)

print(max(lista), min(lista))
print(sorted(lista))