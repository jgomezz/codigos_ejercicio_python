
class Instituto:

    def __init__(self, name , district):

        self.name =  name  # atributo nombre 
        self.district =  district
        

    def getName(self):
        return self.name
    

# Programa Principal
if __name__ == '__main__' :
    
    mi_instituto  = Instituto("Tecsup Centro","Santa Anita")

    print(mi_instituto.name)

    print(mi_instituto.getName())
