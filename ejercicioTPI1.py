A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
ambas_plataformas = []
al_menos_una_plataforma = []

#for i in range (0, len(A)):
#    if A[i] in B:
 #       ambas_plataformas.append(A[i]) 

for i in range (0, len(A)):
    for j in range (0, len(B)):
        if A[i] == B[j]:
            bandera = 0



print("Utilizan al menos una plataforma: ", al_menos_una_plataforma)