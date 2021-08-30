#
# retangulo.py : Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível 2 – Fase 2
#            Uma solução para o problema 'Retangulo'
# Github   : 
# data     : 29/08/2021
# autor    : Professor Flávio Augusto de Freitas,
#            IFSEMG/DACC/Ciência da Computação
# linguagem: Python 3.9.1 64-bit
# hardware : MacBook Pro (Retina, 13-inch, Mid 2014)
#            mac OS Big Sur 11.4
#            2,6 GHz Intel Core i5 Dual-Core
#            8 GB 1600 MHz DDR3
#
#

from itertools import product

#
# criar os arquivos de entrada e saída
#
# arqNprova.[in | sol] = arquivos do pdf da prova, N = número
# arqNobi.[in | sol]   = arquivos do solver da OBI, N = número
#
fin  = open('arq2prova_retangulo.in' , 'r') # arquivo de entrada
fout = open('arq2prova_retangulo.sol', 'w') # arquivo de saída

N = int(fin.readline())
if N < 4 or N > 10 ** 5:
  print('ERRO: Número de árvores inconsistente...\n')
  exit()

L = fin.readline().split(' ')
for i in range(N):
  print(L[i] + '; ', end='')
  if int(L[i]) < 1 or int(L[i]) > 10 ** 6:
    print('ERRO: Valor do arco deve estar entre 1 e 10^6...\n')
    exit()

print('\n')

#
# Dada uma partição esta função soma os arcos (2ª linha do arquivo de entrada)
# de acordo com as quantidades dada pela partição. Por exemplo:
# Uma partição [ 1, 2, 2, 4 ] devolverá uma soma de 1 arco, seguida pela soma
# dos dois próximos arcos, seguida pela soma dos dois próximos arcos, seguida
# pela soma dos 4 próximos arcos. Assim, se os valores da segunda linha forem
# [ 1, 1, 2, 3, 3, 4, 1, 1, 3 ] a soma será [ 1, 3, 6, 9 ], que nesse caso não
# forma retângulo, pois 1 != 6 e 3 != 9, ou seja, não possui lados paralelos
# iguais.
#
def soma_arcos(particao):
  lista = []
  p = 0
  for n in particao:
    soma = 0
    for k in range(int(n)):
      if p + k < len(L):
        soma += int(L[p + k])
    lista.append(soma)
    p += int(n)

  return lista
  

#
# O matemático Ramanujan é famoso por sua fórmula para calcular o número de
# partições de um número natural. Por exemplo:
# As cinco partições de 4 são:
#     4 = 3 + 1             = 2 + 2                 = 2 + 1 + 1 = 1 + 1 + 1 + 1
# E as onze partições de 6 são:
#     6 = 5 + 1             = 4 + 2                 = 4 + 1 + 1 = 3 + 3 
#       = 3 + 2 + 1         = 3 + 1 + 1 + 1         = 2 + 2 + 2 = 2 + 2 + 1 + 1 
#       = 2 + 1 + 1 + 1 + 1 = 1 + 1 + 1 + 1 + 1 + 1
# Esta função devolve todas as partições do número N, dado no arquivo de entrada
def partition(number):
  answer = set()
  answer.add((number, ))
  for x in range(1, number):
    for y in partition(number - x):
      answer.add(tuple(sorted((x, ) + y)))
  return answer


#
# permuta as particoes geradas por partition
#
def pparticoes(particoes):
  pp = []
  # retorna todas as permutacoes para todas as particoes >= 4
  for particao in particoes:
    permsList = [' '.join(str(i) for i in x) for x in product(particao, repeat=len(particao))]
    for item in permsList:
      l = item.split(' ')
      if len(l) >= 4:
        pp.append(l)
  return pp


particoes = partition(N)
particoes_permutadas = pparticoes(particoes)
lista_particoes = []
for particao_permutada in particoes_permutadas:
  if len(particao_permutada) >= 4: # só nos interessa 4 lados dos retângulos
    lista_particoes.append(soma_arcos(particao_permutada))

forma_retangulo = False
for p in lista_particoes:
  if len(p) == 4:
    print(p[0], p[2], p[1], p[3])
    if int(p[0]) == int(p[2]) and int(p[1]) == int(p[3]):
      forma_retangulo = True
        
if forma_retangulo:
  fout.write('S')
else:
  fout.write('N')

fin.close()
fout.close()