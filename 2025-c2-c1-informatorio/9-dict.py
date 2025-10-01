# en funcion del nombre del mes quiero que me diga
# a que numero corresponde
# por ej. agosto --> 8

Calendario = {
    'enero': '1',
    'febrero': '2',
    'marzo': '3',
    'abril': '4',
    'mayo': '5',
    'junio': '6',
    'julio': '7',
    'agosto': '8',
    'septiembre': '9',
    'octubre': '10',
    'noviembre': '11',
    'diciembre': '12'
}

# mes = input("Ingrese el nombre del mes: ").lower()

# if mes in Calendario:
#     print(f'El mes que digito es de numero: {Calendario[mes]}')
# else:
#     print("El mes ingresado no es valido")

# valor_ing = input("Ingrese un numero para determinar el mes")

# for clave, valor in Calendario.items():
#     # print(clave, valor)
#     if valor_ing == valor:
#         print("La clave es:", clave)

swapped_dict = {value: key for key, value in Calendario.items()}

print(swapped_dict)