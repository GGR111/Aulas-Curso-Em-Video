nome = input('Qual é o seu nome? ').title().strip()
if nome == 'Gabriel':
    print('Seu gostoso!!!')
elif nome == 'Jaqueline':
    print('Eu te amo jaqueee')
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('No brasil o seu nome é muito popular!!')
elif nome in 'Karmensita Nicolly Eva Vanere':
    print('Belo nome!!')
else:
    print('Que merda em!')

print('Tenha um bom dia, {}!'.format(nome))