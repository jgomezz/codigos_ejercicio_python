#                 0        1       2
estudiantes = ("Diego" ,"Jaime","Maribel","Pedro","Virginia","Lucero")

print(estudiantes[0])
print(estudiantes[1])

print(estudiantes[-1])

tamanho = len(estudiantes)
print(estudiantes[tamanho-1])

print(estudiantes[0::2])


mi_tupla_1 = (3,4,5,6,7,8,9,10,11,12,13)

nro_impares = mi_tupla_1[0::2]

print(nro_impares)

suma = 0
for tmp in nro_impares:
    suma = suma + tmp
    #print(tmp)

print(f"la suma es {suma}")

suma2 = sum(nro_impares)

print(f"la suma es {suma2}")

min_valor = min(nro_impares)
max_valor = max(nro_impares)

diff = max_valor - min_valor
print(f"la diferencia es {diff}")

