numero = int(input('Criar uma tabela pro número: '))

print('-' * 15)
for i in range(1, 11):
    print(f'\033[1;33m {number} * {i:2} = {number * i:2} \033[m')
print('-' * 15)