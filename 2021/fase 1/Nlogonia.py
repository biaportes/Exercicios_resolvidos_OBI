vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input()

sifra = []
for i in palavra:
    #as vogais não são modificadas
    if i in vogais:
        sifra += i
    #se consoante
    else:
        #a. inicia com a própria consoante
        sifra += i

        #b. busca vogal mais próxima 
        consAscii = ord(i) #transformar a letra em decimal ascii
        
        menordist = 26 #iniciei com valor alto: tamanho do alfabeto
        proximaVogal = ''
        for j in vogais:
            distAtual = abs(consAscii - ord(j))
            if distAtual < menordist:
                menordist = distAtual
                proximaVogal = j
        sifra += proximaVogal

        #c. busca próxima consoante
        proximaConsoante = consAscii
        if proximaConsoante != 122: #vê se é diferente de 'z'
            proximaConsoante += 1
            if chr(proximaConsoante) in vogais :
                proximaConsoante += 1
        sifra += chr(proximaConsoante)

#imprime a lista como string
print(''.join(sifra))

        
