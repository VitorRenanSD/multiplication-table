def multiplicationTable(num):
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')

chosenNumber = int(input('Create a multiplication table to number: '))
multiplicationTable(chosenNumber)