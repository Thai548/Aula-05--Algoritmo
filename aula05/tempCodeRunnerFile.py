valor = float (input('Valor da Compra:'))
print ("""
ESCOLHA A FORMA DE PAGAMENTO:
1 - Pix (12% de desconto)
2 - Débito (8% de desconto)
3 - Crédito (5% de desconto)
4 - Dinheiro (15% de desconto)
""")

opcao = int (input ('Escolha o número de acordo com a forma de pagamento: '))
desconto = 0
match opcao:
    case 1:
        desconto = valor * 0.12
        print('\n---Pagamento no Pix---')
    case 2:
        desconto = valor * 0.08
        print('\n---Pagamento no Débito---')
    case 3:
        desconto = valor * 0.05
        print('\n---Pagamento no Crédito---')
    case 4:
        desconto = valor * 0.15
        print('\n---Pagamento no Dinheiro---')
    case _:
        print('Opção Inválida!')


if desconto != 0:
    valor_final = valor - desconto
    print(f'Valor sem desconto:  {valor}')
    print(f'Valor do desconto:  {desconto}')
    print(f'Valor com desconto: {valor_final}')


else:
    print('Dígite opções válidas informadas acima:')