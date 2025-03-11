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