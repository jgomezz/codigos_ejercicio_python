
class Universidad:

    pais = "Peru"

    def __init__(self, nombre, sede, telefono, direccion, ruc):
        self.nombre = nombre
        self.sede = sede
        self.telefono = telefono
        self.direccion = direccion
        self.ruc = ruc


# Programa Principal
if __name__ == '__main__' :
    
    mi_universidad = Universidad("UNI","Lima", 8333333, "Rimac", "1243347")

    print(mi_universidad.nombre)
    print(mi_universidad.pais)

    mi_universidad_2 = Universidad("San Marcoc","Lima", 1333333, "San Miguel", "12433427")

    print(mi_universidad_2.nombre)
    print(mi_universidad_2.pais)

    Universidad.pais = "Bolivia" 
    print(mi_universidad_2.pais)
    print(mi_universidad.pais)
