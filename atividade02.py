# Atividade 2  - Match case

numero = float(input('Informe o número: '))

match numero:
    case n if n < 0:
        print('Negativo')
    case n if n > 0:
        print('Positivo')
    
    case _: 
        print('Neutro')



