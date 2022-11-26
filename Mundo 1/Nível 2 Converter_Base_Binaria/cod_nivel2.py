num = int(input('Digite seu número inteiro: '))
print(' "1" Para converter seu número para BINÁRIO ? ')
opc = int(input('Resposta: '))
if opc == 1:
    elt = str('BINÁRIO')
else:
    print('Essa opção não é valida!')
if 1 == opc:
    print("O número {} convertido para {}".format(num, elt), end=' ')

print("é igual a {}".format(bin(num)[2:]))
