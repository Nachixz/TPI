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
def ambas_plataformas():
    for i in range (0, len(A)):
        if A[i] in B:
            ambas_plataformas.append(A[i]) 

#Usuarios que usan al menos una plataforma:
def al_menos_una():
    for i in range (0, len(A)):
        if A[i] not in al_menos_una_plataforma:
            al_menos_una_plataforma.append(A[i])

    for i in range (0, len(B)):
        if B[i] not in al_menos_una_plataforma:
            al_menos_una_plataforma.append(B[i])

#Usuarios que no tienen errores:
def sin_errores():
    for i in range (0, len(al_menos_una_plataforma)):
        if al_menos_una_plataforma[i] not in C:
            sin_errores.append(al_menos_una_plataforma[i])

#Usuarios que usan exclusivamente una plataforma:
def solo_una():
    for i in range (0, len(al_menos_una_plataforma)):
        if al_menos_una_plataforma[i] not in ambas_plataformas:
            una_sola_plataforma.append(al_menos_una_plataforma[i])

#Usuarios que tienen errores pero no usan ninguna plataforma:
def errores_sin_plataforma():
    for i in range (0, len(C)):
        if C[i] not in al_menos_una_plataforma:
            errores_sin_plataforma.append(C[i])

print("Usuarios que usan ambas plataformas: ", ambas_plataformas)
print("Usuarios que usan al menos una plataforma: ", al_menos_una_plataforma)
print("Usuarios que no tienen errores: ", sin_errores)
print("Usuarios que usan exclusivamente una plataforma: ", una_sola_plataforma)
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

opcion = 0

while opcion != 8:

    print("\nMENU")
    print("1- Ambas plataformas")
    print("2- Al menos una plataforma")
    print("3- Sin errores")
    print("4- Una sola plataforma")
    print("5- Errores sin plataforma")
    print("6- Clasificación")
    print("7- Matrices")
    print("8- Salir")

    opcion = int(input("Ingrese una opcion: "))
  
    if opcion == 1:
        ambas_plataformas()
        print(ambas_plataformas)

    elif opcion == 2:
        al_menos_una()
        print(al_menos_una_plataforma)

    elif opcion == 3:
        al_menos_una()
        sin_errores()
        print(sin_errores)

    elif opcion == 4:
        al_menos_una()
        ambas_plataformas()
        solo_una()
        print(una_sola_plataforma)

    elif opcion == 5:
        al_menos_una()
        errores_sin_plataforma()
        print(errores_sin_plataforma)

    elif opcion == 6:
        usuarios_ayb()
        clasificacion_de_usuario()

    elif opcion == 7:
        promedio_por_funcion()
        promedio_por_servidor()
        matriz_transpuesta()

    elif opcion == 8:
        print("Fin")

    else:
        print("Opcion incorrecta")