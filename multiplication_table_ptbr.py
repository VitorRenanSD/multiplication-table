def multiplicationTable(num):
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')

numeroEscolhido = int(input('Criar uma tabela para o número: '))
multiplicationTable(numeroEscolhido)
