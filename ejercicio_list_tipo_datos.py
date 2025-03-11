valor = 10

print(type(valor))

if type(valor) == int :
    print("Es entero")
elif type(valor) == float :
    print("Es deciaml")
else : 
    print("NO identificable")

# Calcular la suma de enteros y decimales
data = [45, 12.4, 1.13, 45, 4.5, 20, 1.8, 5.6, 14]

nros_ent = []
nros_dec = []

for item in data:
    if type(item) == int :
        nros_ent.append(item)
    elif type(item) == float :
        nros_dec.append(item)

print(sum(nros_ent))
print(sum(nros_dec))

