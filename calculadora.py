continuar= True

while continuar:
    print('-='*10,'ESCOLHA UMA OPÇÃO','=-'*10)
    for i in range(1):
        print('')
    print('(1) soma','/','(2) subtrair','/','(3) multiplicar','/','(4) dividir')
    print('')
    opcao=int(input('ESCOLHA 1/2/3/4 :'))
    print('')
    numero1 = float(input('DIGITE O NUMERO: '))
    print('')
    numero2 = float(input('DIGITE O NUMERO: '))

    if (opcao == 1):
        soma=numero1 + numero2
        print('')
        print('RESULTADO =',soma)
    if (opcao == 2):
        subtrair = numero1 - numero2
        print('')
        print('RESULTADO =',subtrair)
    if (opcao == 3):
        multiplicar = numero1 * numero2
        print('')
        print('RESULTADO =',multiplicar)
    if(opcao == 4):
        dividir = numero1 / numero2
        print('')
        print('RESULTADO =',dividir)
    print('')
    if (opcao >= 5):
        print('OPÇÃO NÃO ENCONTRADA')
        print('')
    parar=input('DESEJA CONTINUAR? (S/N): ').lower()
    print('')
    if parar == 'n':
        continuar = False
        
print('Fechando..............')


















    
