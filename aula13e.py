s = 1
f = int(input('digite o fim: '))
for a in range(1, f+1):
    n = int(input('[ {} ] Digite o numero numero: '.format(a)))
    s += n
print(s)
