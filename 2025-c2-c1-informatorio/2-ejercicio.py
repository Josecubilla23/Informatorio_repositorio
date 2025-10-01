# Determinar si el usuario, el cual
# ingresa por pantalla su anho de nacimiento
# es mayor o menor de edad

anho_usuario = int(input('Ingrese su anho de nacimiento: '))
anho_actual = 2025

edad = anho_actual - anho_usuario

mayor_edad = 17

if (edad > mayor_edad):
    print('El usuario tiene mayoria de edad')
else:
    print('El usario es menor de edad')

