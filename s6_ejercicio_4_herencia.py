
class Auto:


    def __init__(self,  marca, color, anho ,garantia, ciudad ):
        self.marca = marca
        self.color = color
        self.anho = marca
        self.anho = anho
        self.garantia = garantia
        self.ciudad = ciudad


    def obtener_informacion(self):
         
         return self.name


class SUV (Auto):
    pass

class Seddan (Auto):
    pass

class VAN (Auto):
    pass

# Programa Principal
if __name__ == '__main__' :

    mi_auto  = SUV("Toyota","Negro",1999, 2, "Lima")

    print(mi_auto.marca)
    print(mi_auto.anho)
