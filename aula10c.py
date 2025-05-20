n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m >= 7:
    print('Sua media foi: {:.2f}, Aprovado!'.format(m))
else:
    print('Sua media foi: {:.2f}, Reprovado!'.format(m))
