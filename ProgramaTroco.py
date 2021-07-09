import locale
locale.setlocale(locale.LC_MONETARY , 'pt_BR.utf-8')
print('=' * 50)
print('{:^50}'.format('CAIXA'))
print('='* 50)
compra = float(input('Qual o valor da compra? R$ '))
pagamento = float(input('Qual o valor do pagamento? R$ '))
troco = (pagamento - compra)
ced = 50
totced = 0
total = troco

if troco > 0:
    print('O troco foi de R$ {:.2f}' .format(troco))
elif troco == 0:
    print('O valor está correto, não precisa de troco!')    
else:
    print('Ficou faltando R$ {:.2f}' .format(-troco))


while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula(as)/moeda(as) de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        elif ced == 1:
            ced = 0.50
        elif ced == 0.50:
            ced = 0.25
        elif ced == 0.25:
            ced = 0.10
        elif ced == 0.10:
            ced = 0.05
        elif ced == 0.05:
            ced = 0.01
        totced = 0
        if total == 0:
            break
print ('=' * 50)
print ('{:^50}'.format('Operação finalizada!'))