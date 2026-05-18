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
for i in range (0, len(A)):
    if A[i] in B:
        ambas_plataformas.append(A[i]) 

#Usuarios que usan al menos una plataforma:
for i in range (0, len(A)):
    if A[i] not in al_menos_una_plataforma:
        al_menos_una_plataforma.append(A[i])

for i in range (0, len(B)):
    if B[i] not in al_menos_una_plataforma:
        al_menos_una_plataforma.append(B[i])

#Usuarios que no tienen errores:
for i in range (0, len(al_menos_una_plataforma)):
    if al_menos_una_plataforma[i] not in C:
        sin_errores.append(al_menos_una_plataforma[i])

#Usuarios que usan exclusivamente una plataforma:
for i in range (0, len(al_menos_una_plataforma)):
    if al_menos_una_plataforma[i] not in ambas_plataformas:
        una_sola_plataforma.append(al_menos_una_plataforma[i])

#Usuarios que tienen errores pero no usan ninguna plataforma:
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

for i in range (0, len(A)):
    if A[i] not in usuarios:
        usuarios.append(A[i])

for i in range (0, len(B)):
    if B[i] not in usuarios:
        usuarios.append(B[i])

#Clasificacion de usuarios:
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