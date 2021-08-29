
N = int(input())

valores = []
for i in range(N):
    v = int(input())
    if( v == 0):
        valores = valores[:-1]
    else:
        valores.append(v)

print(sum(valores))
