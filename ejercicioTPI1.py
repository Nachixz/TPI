# Conjuntos:

A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
ambas_plataformas = []
al_menos_una_plataforma = []
sin_errores = []
una_sola_plataforma = []
errores_sin_plataforma = []

#Usuarios que usan ambas plataformas:
def ambas_plataformass():
    for i in range (0, len(A)):
        if A[i] in B:
            ambas_plataformas.append(A[i]) 
    print("Usuarios que usan ambas plataformas: ", ambas_plataformas)

#Usuarios que usan al menos una plataforma:
def al_menos_una():
    for i in range (0, len(A)):
        if A[i] not in al_menos_una_plataforma:
            al_menos_una_plataforma.append(A[i])

    for i in range (0, len(B)):
        if B[i] not in al_menos_una_plataforma:
            al_menos_una_plataforma.append(B[i])
    print("Usuarios que usan al menos una plataforma: ", al_menos_una_plataforma)

#Usuarios que no tienen errores:
def sin_erroress():
    for i in range (0, len(al_menos_una_plataforma)):
        if al_menos_una_plataforma[i] not in C:
            sin_errores.append(al_menos_una_plataforma[i])
    print("Usuarios que no tienen errores: ", sin_errores)


#Usuarios que usan exclusivamente una plataforma:
def solo_una():
    for i in range (0, len(al_menos_una_plataforma)):
        if al_menos_una_plataforma[i] not in ambas_plataformas:
            una_sola_plataforma.append(al_menos_una_plataforma[i])
    print("Usuarios que usan exclusivamente una plataforma: ", una_sola_plataforma)

#Usuarios que tienen errores pero no usan ninguna plataforma:
def errores_sin_plataformaa():
    for i in range (0, len(C)):
        if C[i] not in al_menos_una_plataforma:
            errores_sin_plataforma.append(C[i])
    print("Usuarios que tienen errores pero no usan ninguna plataforma: ", errores_sin_plataforma)

#Logica:

#Union A y B:

usuarios = []
def usuarios_ayb():
    for i in range (0, len(A)):
        if A[i] not in usuarios:
            usuarios.append(A[i])

    for i in range (0, len(B)):
        if B[i] not in usuarios:
            usuarios.append(B[i])
    print(usuarios)

#Clasificacion de usuarios:
def clasificacion_de_usuario():
    criticos = []
    no_criticos = []

    for i in range (0, len(usuarios)):

        usuario = usuarios[i]

        p = usuario in A
        q = usuario in B
        r = usuario in C

        # (p OR q) AND r
        if (p or q) and r:
            criticos.append(usuario)
        else:
            no_criticos.append(usuario)

    print("Usuarios criticos: ", criticos)
    print("Usuarios no criticos: ", no_criticos)


#MATRICES

M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

def ver_matriz():
    print("Matriz:")
    for fila in M:
        print(fila)

# PROMEDIO POR FUNCION
def promedio_por_funcion():

    print("PROMEDIO POR FUNCION")

    for i in range(0, len(M)):

        suma = 0

        for j in range(0, len(M[i])):
            suma = suma + M[i][j]

        promedio = suma / len(M[i])

        print("Funcion", i + 1, ":", promedio, "ms")


# PROMEDIO POR SERVIDOR
def promedio_por_servidor():

    print("PROMEDIO POR SERVIDOR")

    for j in range(0, len(M[0])):

        suma = 0

        for i in range(0, len(M)):
            suma = suma + M[i][j]

        promedio = suma / len(M)

        print("Servidor", j + 1, ":", promedio, "ms")
        

# MATRIS TRANSPUESTA
def matriz_transpuesta():
    transpuesta = []

    for j in range(len(M[0])):
        fila = []

        for i in range(len(M)):
            fila.append(M[i][j])

        transpuesta.append(fila)

    print("\nMATRIZ TRANSPUESTA")

    for fila in transpuesta:
        print(fila)

#MENU
def menu():
    opcion = ""

    while opcion != "4":

        print("\n---MENU---")
        print("Que opcion desea ejecutar?")
        print("Opcion 1 - Conjuntos")
        print("Opcion 2 - Logica")
        print("Opcion 3 - Matrices")
        print("Opcion 4 - Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            opcion_conjuntos = ""
            while opcion_conjuntos != "6":
                print("\n---Conjuntos---")
                print("Opcion 1 - Usuarios que utilizan ambas plataformas")
                print("Opcion 2 - Usuarios que usan al menos una plataforma(Tiene que ejecutar esta opcion antes de elegir las que siguen)")
                print("Opcion 3 - Usuarios que no tienen errores")
                print("Opcion 4 - Usuarios que usan exclusivamente una plataforma")
                print("Opcion 5 - Usuarios que presentan errores pero no usan ninguna plataforma")
                print("Opcion 6 - Salir")

                opcion_conjuntos = input("Ingrese una opcion: ")

                match opcion_conjuntos:
                    case "1":
                        ambas_plataformass()
                    case "2":
                        al_menos_una()
                    case "3":
                        sin_erroress()
                    case "4":
                        solo_una()
                    case "5":
                        errores_sin_plataformaa()
                    case "6":
                        exit
        elif opcion == "2":
            opcion_logica = ""
            while opcion_logica != "3":
                print("\n---Logica---")
                print("Opcion 1 - Hacer union A y B")
                print("Opcion 2 - Ver clasificacion de usuarios")
                print("Opcion 3 - Salir")

                opcion_logica = input("Eliga una opcion: ")
                match opcion_logica:
                    case "1":
                        usuarios_ayb()
                    case "2":
                        clasificacion_de_usuario()
                    case "3":
                        exit
        elif opcion == "3":
            opcion_matrices = ""
            while opcion_matrices != "5":
                print("\n---Matrices---")
                print("Opcion 1 - Ver matriz")
                print("Opcion 2 - Calcular promedio por funcion")
                print("Opcion 3 - Calcular promedio por servidor")
                print("Opcion 4 - Matriz transpuesta")
                print("Opcion 5 - Salir")

                opcion_matrices = input("Ingrese una opcion: ")
                match opcion_matrices:
                    case "1":
                        ver_matriz()
                    case "2":
                        promedio_por_funcion()
                    case "3":
                        promedio_por_servidor()
                    case "4":
                        matriz_transpuesta()
                    case "5":
                        exit
        elif opcion == "4":
            print("Gracias por usar este programa!")
            exit
        else:
            print("Opcion incorrecta")

#MENU
menu()