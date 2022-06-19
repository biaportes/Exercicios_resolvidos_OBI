dias = 31

D = int(input()) #valor da diária
A = int(input()) #aumento da diária
N = int(input()) #dia da chegada do hóspede

if N == 1:
    valor = 31*(D)
elif N >=2 and N<=15:
    valor = (dias-N + 1)*(D + (N-1)*A)
else:
    valor = (dias-N + 1)*(D + 14*A)

print(valor)
