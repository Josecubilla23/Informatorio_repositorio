# x = 100

# for x in range(-1, 10):
#     print(x)

# print(x)

var_est_list = [1, 2, 3, 4, 5, 'pepe', 'pepito']

for var in var_est_list:
    if isinstance(var, int):
        print(var + 1)
    else:
        print(var)
