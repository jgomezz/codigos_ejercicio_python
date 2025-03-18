
class Instituto:

    def __init__(self, name , district):
        self.name =  name  # atributo nombre 
        self.district =  district

    def getName(self):
        return self.name


class Universidad:

    def __init__(self, nombre, sede, telefono, direccion, ruc):
        self.nombre = nombre
        self.sede = sede
        self.telefono = telefono
        self.direccion = direccion
        self.ruc = ruc


# Programa Principal
if __name__ == '__main__' :
    
    mi_instituto  = Instituto("Tecsup Centro","Santa Anita")

    print(mi_instituto.name)
    print(mi_instituto.getName())

    mi_universidad = Universidad("UNI","Lima", 8333333, "Rimac", "1243347")

    print(mi_universidad.nombre)
