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









