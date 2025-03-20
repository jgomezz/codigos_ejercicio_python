
class Auto:


    def __init__(self,  marca, color, anho ,garantia, ciudad ):
        self.marca = marca
        self.color = color
        self.anho = anho
        self.garantia = garantia
        self.ciudad = ciudad


    def obtener_informacion(self):
         
         return self.marca


class SUV (Auto):

    def obtener_informacion(self):
         
         return self.ciudad

class Seddan (Auto):
    pass

class VAN (Auto):
    pass

# Programa Principal
if __name__ == '__main__' :

    mi_auto  = SUV("Toyota","Negro",1999, 2, "Lima")

    print(mi_auto.marca)
    print(mi_auto.anho)
    print("DEBUG3" + mi_auto.obtener_informacion())

    mi_mov_escolar = VAN("Nissan","Negro",2012, 5, "Lima")

    print(mi_mov_escolar.marca)
    print(mi_mov_escolar.anho)
    print("debuf1m"  + mi_mov_escolar.obtener_informacion())
