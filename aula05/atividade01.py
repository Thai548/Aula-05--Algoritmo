
#Atividade 01
        #Escreva um programa que leia o codigo de oriegem do produto e imprima na tela a região de sua procedência:

codigo = int(input('Informe o código de acordo com o destino desejado:  '))

match codigo:
    case 1:
        print ('Sul')
    case 2:
        print ('Norte')
    case 3:
        print ('Leste')
    case 4:
        print ('Oeste')
    case 5 | 6:
        print ('Nordeste')
    case 7 | 8 | 9:
        print ('Sudeste')
    case 10:
        print ('Centro-Oeste')
    case 11:
        print ('Noroeste')
    case _:
        print('Destino não localizado') 