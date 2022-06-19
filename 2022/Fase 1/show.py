#N = filas
#M = assentos por fila
#A = número de amigos
A, N, M = input().split()
A = int(A)
N = int(N)
M = int(M)

achou = -1
for i in range(N, 0, -1):
    linha = input().split()
    cont = 0
    for assento in linha:
        if assento == '0':
            cont+=1
            #print('entrou')
            if cont == A:
                achou = i
                #print('entrou2')
        else:
            cont = 0
            #print('entrou3')

print(achou)
