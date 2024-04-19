count = result = 0

while True:
    num = int(input('Create a multiplication table to number: '))
    if num < 0:
        print('END')
        break
    print('-' * 20)
    while count < 10:
        count += 1
        result = num * count
        print(f'{num} x {count:2} = {result}')
    count = 0
    print('-' * 20)
