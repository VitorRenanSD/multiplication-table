number = int(input('Create a multiplication table to number: '))

for i in range(1, 11):
    print(f'{number} * {i:2} = {number * i}')
