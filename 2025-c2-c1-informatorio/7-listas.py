# validar si en la siguiente lista existen dos numeros
# contiguos que su suma de el valor de target
#           0  1  2  3 4 5 6 7 8 9 10 11 12 13
lista = [5,1002,32,12,32,7,1,2,3,4,6,7, 8, 9, 0,10]
target = 12

posiciones = len(lista) - 1
# print(posiciones[14])
cumple = False
for pos in range(0, posiciones):
    for prx in range(pos + 1, posiciones):
        suma = lista[pos] + lista[prx]
        if (suma == target):
            cumple = True
            print("El valor de la posicion:", pos, "y la posicion:", prx,"dan igual al target")

if (not cumple):
    print("Ninguno de los valores suman lo del target")
