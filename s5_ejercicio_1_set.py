
nombres_estudiantes = ["Jaime","Juana","Rocio","Rebeca","Jaime","Jaime","Rocio","Juan"]

nombres_estudiantes_unicos = set(nombres_estudiantes)

print(nombres_estudiantes_unicos)

for nombre in nombres_estudiantes_unicos:
     
     cont = 0
     for _nombre in nombres_estudiantes:
          if nombre == _nombre:
               cont = cont  + 1
               
     print(f" {nombre} es usado {cont} veces" )