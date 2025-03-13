
participantes = {
    1: "Jose",
    2: "Alberto",
    3: "Erick",
    4: "Juana",
    5: "Maria"
}
print(participantes[4])

participantes[6] ="Patricia"

print(participantes)

print(participantes.keys())

print(participantes.values())

print(participantes.items())


participantes = {
    1: {
        "nombre":"Jose",
        "apellido":"Perez",
        "edad":34
        },
    2: {
        "nombre":"Alberto",
        "apellido":"Garcia",
        "edad":25
        },
    3: "Erick",
    4: "Juana",
    5: "Maria"
}


np1 = participantes[1]["nombre"]
ep2 = participantes[2]["edad"]

print(np1)
print(ep2)