frase = 'Curso em video Python'
#encontra o caractere desejado
print (frase[9])
#encontra do caractere desejado até o outro caractere desejado
print (frase[9:13])
#encontra do caractere desejado até o outro caractere desejado pulando de 2 em 2 caracteres
print (frase[9:21:2])
#encontra do inicio da frase até o caractere desejado
print (frase[:5])
#encontra do caractere desejado até o fim da frase
print (frase[15:])
#encontra do caractere desejado até o fim da frase pulando de 3 em 3
print (frase[9::3])
#conta quantos caracteres tem
print (len(frase))
#conta quantas letras O tem
print (frase.count('o'))
#conta quantas letras O tem começando do inicio até o caractere desejado
print (frase.count('o',0,13))
#encontra onde inicia o palavra ou caractere desejado
print (frase.find('deo'))
print (frase.find('android'))
#responde com true ou false se tem a palavra ou caractere desejado
print ('Curso' in frase)
#substitui o caractere ou frase desejado
print (frase.replace(' ','/'))
#deixa tudo maiusculo
print (frase.upper())
#deixa tudo minusculo
print (frase.lower())
#faz apenas a primeira letra da frase inteira ser maiuscula
print (frase.capitalize())
#faz a primeira letra de cada palavra ficar maiuscula
print (frase.title())
frase2 = '   Aprenda Python  '
#cancela espaços inuteis do inicio da frase e do final
print (frase2.strip())
#cancela os espaços inuteis da direita do texto
print (frase2.rstrip())
#cancela os espaços inuteis da esquerda do texto
print (frase2.lstrip())
#cria uma divisão entre os espaços
print (frase.split())
#junta entre os espaços com um caractere
print ('-'.join(frase.split()))