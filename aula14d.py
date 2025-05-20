sp = 0
si = 0
n = 1
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0 and n != 0:
            sp +=1
        else:
            si +=1
print('Foram digitados {} numeros pares e {} numero impares'.format(sp,si))