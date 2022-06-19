from subprocess import Popen
from subprocess import PIPE
import os

# pasta do gabarito baixada do site da OBI para submeter o algoritmo a teste
questao = 'show'
fase_nivel = "2022f1p1_"
path= fase_nivel + questao+"/"
OBI_solution = questao+'.py'

#for num_pasta in range(1,6):
#  for num_arq in range(1,5):
for diretorio, subpastas, arquivos in os.walk(path):
    for arquivo in arquivos:
        if arquivo[-2:] == 'in':
            nome_arquivo = os.path.join(diretorio, arquivo)

            args= ['python3', OBI_solution]

            p1 = Popen(["cat", nome_arquivo], stdout=PIPE)
            p2 = Popen(args, stdin=p1.stdout, stdout=PIPE)
            p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
            output = p2.communicate()[0]

            with open(nome_arquivo[0:-2]+"sol") as fsaida:
                saida = fsaida.readlines()
            output = str(output.decode('utf-8')[0:-1])
            saida = str(saida[0][0:-1])

            if saida == output:
                print('iguais')

            else:
                print('diferentes', saida, output)
