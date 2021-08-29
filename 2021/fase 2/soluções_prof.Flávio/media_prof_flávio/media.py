#
# media.py : Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível 2 – Fase Fase 2
#            Uma solução para o problema 'Média e Mediana'
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

#
# criar os arquivos de entrada e saída
#
# arqNprova.[in | sol] = arquivos do pdf da prova, N = número
# arqNobi.[in | sol]   = arquivos do solver da OBI, N = número
#
fin  = open('arq2prova_media.in' , 'r') # arquivo de entrada
fout = open('arq2prova_media.sol', 'w') # arquivo de saída

line = fin.readline()

A = int(line.split(' ')[0])
print(str(A) + ' lido...')
if A < 1:
  print('ERRO: A deve ser maior ou igual que 1...\n')
  exit()

B = int(line.split(' ')[1])
print(str(B) + ' lido...')
if B < A:
  print('ERRO: B deve ser maior ou igual que A...\n')
  exit()

if B > 10 ** 9:
  print('ERRO: B deve ser menor ou igual que 10^9...\n')
  exit()

def med(a, b, c):
  l = [a, b, c]
  l.sort()
  print(l)
  return l[1]

for C in range(0, 10 ** 9, 1):
  media = (A + B + C)/3
  mediana = med(A, B, C)
  if (media == mediana):
    fout.write(str(C))
    break

  media = (A + B - (10 ** 9 - C))/3
  mediana = med(A, B, -(10 ** 9 - C))
  if (media == mediana):
    fout.write(str(-(10 ** 9 - C)))
    break

if (media != mediana):
  fout.write('0')

# fechar os arquivos
fin.close
fout.close