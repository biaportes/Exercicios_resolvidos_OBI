'''
Esse é o mais tranquilo de todos! Ele quer o menor valor para o C no qual média e mediana sejam iguais. Disse ainda que a é menor ou igual a b.
Sabe-se que a média e mediana serão iguais quando a distribuição dos números for simétrico! Se ele quer o menor valor pro C, infere-se que:
c <= a <= b
Assim:
distancia = b - a
c = a - distancia
'''

linha = input()
a, b = linha.split()
a = int(a)
b = int(b)

distancia = b-a
c = a-distancia

print(c)
