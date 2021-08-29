#os números dados representam a proporção do perímetro do circulo
#Não que seja exigência no exercício, mas a soma de todos os arcos tem que ser divisível por 360

#para que se consiga fazer um retângulo, o perímetro de dois lados opostos precisam ser iguais
#vale ainda dizer que não é possível manter um ângulo de 90º entre os lados paralelos se eles não ocuparem quadrantes opostos

ESQUERDA = 0
DIREITA = 1

def buscaPar(lado, valorProcurado, sublista):
    arcos = []
    inicio= fim= incrementa = []

    #caminha de trás pra frente
    if lado == DIREITA:
        incrementa = -1
        inicio = len(sublista) - 1
        fim = -1
    #caminha de frente pra trás
    else:
        incrementa = 1
        inicio = 0
        fim = len(sublista)

    aux = 0

    for i in range(inicio, fim, incrementa):
        aux += sublista[i][1]
        arcos.append(sublista[i])
        if valorProcurado < aux:
            i = arcos[0][0] - 1

            arcos = []
            aux = 0
        elif valorProcurado == aux:

            return arcos

    return []

def caminha_lado(lado, valorProcurado, sublista):
    retorno_busca = buscaPar(lado, valorProcurado, sublista)
    limite_superior_prox_busca = []
    if retorno_busca != []:
        #a lista retornada vai do maior índice até o menor
        #peguei o último índice da lista (menor índice) e subtraí um
        # a próxima busca terá esse limite superior
        tam = len(retorno_busca)-1
        limite_superior_prox_busca = retorno_busca[tam][0]


    return limite_superior_prox_busca


arvores = int(input())
arcos_arvores = input()
arcos_arvores = arcos_arvores.split()

#converter essa lista em uma lista de inteiros
arcos_arvores = list(map(int, arcos_arvores))

#mais fácil trabalhar com uma matriz de índices e valores
matriz_arvores = []
for i in range(arvores):
     matriz_arvores.append([i, arcos_arvores[i]])

meio = (arvores//2)-1
achou = False

inicio_esq = 0
fim_esq = meio - 1
busca_elem_esq = meio

inicio_dir = meio + 1

#para formar a reta do lado esquerdo e direito, cada lado terá dois pontos -> total 4 que formam o retângulo
#excluí o primeiro elemento porque, no mínimo, ele será o 2º ponto da esquerda
while(achou == False and busca_elem_esq > inicio_esq):
    fim_dir = arvores

    caminha = DIREITA
    aux_dir = caminha_lado(caminha, matriz_arvores[busca_elem_esq][1], matriz_arvores[inicio_dir:fim_dir])
    if aux_dir != []:
        fim_dir = aux_dir
        busca_elem_dir = inicio_dir

        fim_esq = busca_elem_esq
        while(achou == False and busca_elem_dir < fim_dir):
            caminha = ESQUERDA
            aux_esq = caminha_lado(caminha, matriz_arvores[busca_elem_dir][1], matriz_arvores[inicio_esq:fim_esq])
            if aux_esq != []:
                achou = True
                break
            busca_elem_dir += 1

    busca_elem_esq -= 1

if achou:
    print('S')
else:
    print('N')
