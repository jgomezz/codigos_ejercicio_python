
def imprimir_msg(nro_veces = 5) :

    for i in range(nro_veces):
        print(f"Hola mundo {i+1}")


imprimir_msg(5)

imprimir_msg(12)

imprimir_msg(3)

imprimir_msg()


# Funcion de suma


def suma (op1, op2):

    s = op1 + op2

    print(f"La suma es {s}")



suma(13,12)
suma(1,20)


def resta (op1, op2):

    r = op1 - op2

    return r


resultado = resta(13,12)

print(resultado)