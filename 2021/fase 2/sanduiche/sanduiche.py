def retorna_fat(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i +=1
    return fat

linha = input()
n, m = linha.split()

n = int(n)
m = int(m)

parIngred = []
for i in range(m):
    parIngred.append(input())


#Total possibilidades
combina = []
k = 1
while k <= n:
    total = retorna_fat(n)/(retorna_fat(k) * retorna_fat(n-k))
    combina.append(total)
    k += 1

#Total impossibilidades
#considera o par como um elemento
#então n' elementos é igual a n-1
imp_combina = []

if m > 0:
    k = 1
    nl = n-2
    ingred = nl
    while k <= nl:
        total = retorna_fat(nl)/(retorna_fat(k) * retorna_fat(nl-k))
        imp_combina.append(m*total)
        ingred -=1
        k +=1
    imp_combina.append(1)
else:
    imp_combina.append(0)


print(sum(combina) - sum(imp_combina))
