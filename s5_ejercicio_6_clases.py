# Caso 1

# Define la clase
class Humano:
    pass

# Creacion de objetos
Adan = Humano()
Adan.papa = None
Adan.mama = None
Adan.edad = 33

Eva = Humano()
Eva.papa = None
Eva.mama = None
Eva.edad = 32

Abel = Humano()
Abel.papa = Adan
Abel.mama =  Eva
Abel.edad = 10

print(Abel.mama.edad)
print(Abel.papa.edad)
print(Abel.edad)


# Caso 2

print("--------- Caso 2")

# Define la clase
class Humano:

    # Constructor del a clase
    def __init__(self, papa, mama, edad):
        self.papa = papa
        self.mama = mama
        self.edad = edad



Adan = Humano(None, None, 33)

Eva = Humano(None, None, 32)

Abel = Humano(Adan, Eva, 10)

print(Abel.mama.edad)
print(Abel.papa.edad)
print(Abel.edad)