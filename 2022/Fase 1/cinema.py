idade1 = int(input())
idade2 = int(input())
ingresso1=0
if idade1 <= 17:
    ingresso1= 15
elif idade1 <= 59:
    ingresso1= 30
else:
    ingresso1= 20

ingresso2=0
if idade2 <= 17:
    ingresso2= 15
elif idade2 <= 59:
    ingresso2= 30
else:
    ingresso2= 20

print(ingresso1 + ingresso2)
