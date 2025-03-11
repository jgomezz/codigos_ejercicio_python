# Dada las siguientes linea

participantes =  ["Jaime:Gomez:23" ,
"Siliva:Patedes:22",
"Hyan:Garcia:12"]

# Calcular la sumas de las edades

edades = []

for persona in participantes:
    print(persona)
    data = persona.split(":")
    print(data)
    edades.append(int(data[-1]))

print(edades)
print(sum(edades))


'''
msg = "El dia de hoy tenemos clases de Python"

Generar el siguiente mensaje

"El--dia--de--hoy--tenemos--clases--de--Python"

Usar los metodos join y split
'''

msg = "El dia de hoy tenemos clases de Python"

data = msg.split(" ")

print(data)

salida = "--".join(data)

print(salida)


#

nros = [1,2,3,4,5,6,7,8,9,10]
print(nros)

nros = [ i for i in range(1,1001) ]
print(nros)

