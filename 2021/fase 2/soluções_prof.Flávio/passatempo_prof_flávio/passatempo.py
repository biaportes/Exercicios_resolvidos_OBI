#
# passatempotempo.py : Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível 2 – Fase 2
#            Uma solução para o problema 'Passatempo'
# Github   : 
# data     : 26/08/2021
# autor    : Professor Flávio Augusto de Freitas,
#            IFSEMG/DACC/Ciência da Computação
# linguagem: Python 3.9.1 64-bit
# hardware : MacBook Pro (Retina, 13-inch, Mid 2014)
#            mac OS Big Sur 11.4
#            2,6 GHz Intel Core i5 Dual-Core
#            8 GB 1600 MHz DDR3
#
#

import math


#
# criar os arquivos de entrada e saída
#
# arqNprova.[in | sol] = arquivos do pdf da prova, N = número
# arqNobi.[in | sol]   = arquivos do solver da OBI, N = número
#
fin  = open('arq1prova_passatempo.in' , 'r') # arquivo de entrada
fout = open('arq1prova_passatempo.sol', 'w') # arquivo de saída

#
# dicionário temporário que armazenará os valores das variáveis
# {
#   var: valor # variável: valor
# }
#
variaveis = {}
conta_variaveis = {}

line = fin.readline() # números de linhas e colunas do passatempo
L = int(line.split(' ')[0])
# print(L)
if L < 1 or L > 100:
  print('ERRO: L deve estar entre 1 e 100...\n')
  exit()

C = int(line.split(' ')[1])
# print(C)
if C < 2 or C > 100:
  print('ERRO: C deve estar entre 2 e 100...\n')
  exit()

var_mat = [] # matriz de variáveis, conforme o arquivo de entrada
num_mat = [] # matriz numérica (onde as variáveis foram substituídas)
S = [] # soma de cada linha da matriz
X = [] # soma de cada coluna da matriz

#
# processa todas as linhas do arquivo de entrada
#
for i in range(0, L): 
  line = fin.readline() # lê uma linha
  vars = line.split(' ') # cria uma lista com os valores da linha

  S.append(int(vars[C])) # cria uma lista com os valores das somas das linhas

  # checa os limites dos valores 'S' de cada linha
  if int(vars[C]) < -10 ** 8 or int(vars[C]) > 10 ** 8:
    print('ERRO: A soma das linhas deve estar entre -10^8 e 10^8...\n')
    exit()

  var_mat.append(vars[0:C])
  for var in vars[0:C]:
    variaveis[var] = math.nan # cria um dicionário para as variáveis com valores NaN
    conta_variaveis[var] = 0

for i in range(L):
  l = []
  for j in range(C):
    l.append(0)
  num_mat.append(l)

# lê a última linha do arquivo de entrada (com os valores 'Xi')
line = fin.readline()
xis = line.split(' ')

# checa cada valor 'Xi' de cada coluna
for xi in xis:
  X.append(int(xi)) # cria uma lista com os valores das somas das colunas
  if int(xi) < -10 ** 8 or int(xi) > 10 ** 8:
    print('ERRO: A soma das colunas deve estar entre -10^8 e 10^8...\n')
    exit()

variaveis = dict(sorted(variaveis.items())) # dicionário de saída ordenado
conta_variaveis = dict(sorted(conta_variaveis.items()))

# verifica se há algum valor 'NaN' no dicionário
def temVariavelDesconhecida():
  for key in variaveis:
    if math.isnan(variaveis[key]):
      return True
  return False

#
# encontrar todos os valores das variáveis até não sobrar nenhuma variável
# desconhecida no dicionário
#


#
# encontrar uma linha/coluna em que as variáveis desconhecidas sejam apenas uma
#
print('Resolvendo passatempo...')
while temVariavelDesconhecida():
  # encontrar por linhas
  for i in range(L):
    # print('Verificando linha ' + str(i))
    for key in variaveis:
      conta_variaveis[key] = 0
    for j in range(C):
      var = var_mat[i][j]
      if math.isnan(variaveis[var]):
        conta_variaveis[var] += 1

    num_variaveis_desconhecidas = 0
    for key in conta_variaveis:
      if conta_variaveis[key] > 0 and math.isnan(variaveis[key]):
        num_variaveis_desconhecidas += 1

    if num_variaveis_desconhecidas == 1:
      for key in conta_variaveis:
        if conta_variaveis[key] > 0:

          # 1. colocar os valores conhecidos em num_mat
          for var in variaveis:
            if not(math.isnan(variaveis[var])):
              for lin in range(L):
                for col in range(C):
                  if var_mat[lin][col] == var:
                    num_mat[lin][col] = int(variaveis[var])

          # 2. calcular a 'soma' atual da linha i em num_mat para subtrair de S[i]
          soma = 0
          for j in range(C):
            soma += num_mat[i][j]
          variaveis[key] = int((S[i] - soma) / conta_variaveis[key])


  # encontrar por colunas
  for j in range(C):
    # print('Verificando coluna ' + str(j))
    for key in variaveis:
      conta_variaveis[key] = 0
    for i in range(L):
      var = var_mat[i][j]
      if math.isnan(variaveis[var]):
        conta_variaveis[var] += 1

    num_variaveis_desconhecidas = 0
    for key in conta_variaveis:
      if conta_variaveis[key] > 0 and math.isnan(variaveis[key]):
        num_variaveis_desconhecidas += 1

    if num_variaveis_desconhecidas == 1:
      for key in conta_variaveis:
        if conta_variaveis[key] > 0:

          # 1. colocar os valores conhecidos em num_mat
          for var in variaveis:
            if not(math.isnan(variaveis[var])):
              for lin in range(L):
                for col in range(C):
                  if var_mat[lin][col] == var:
                    num_mat[lin][col] = int(variaveis[var])

          # 2. calcular a 'soma' atual da coluna j em num_mat para subtrair de X[j]
          soma = 0
          for i in range(L):
            soma += num_mat[i][j]
          variaveis[key] = int((X[j] - soma) / conta_variaveis[key])

for var in variaveis:
  fout.write(var + ' ' + str(variaveis[var]) + '\n')

fin.close()
fout.close()

print('Passatempo resolvido...')