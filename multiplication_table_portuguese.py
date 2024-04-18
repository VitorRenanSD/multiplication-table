#Mostrar a tabuada para cada numero digitado pelo usuario, o programa ira parar quando o numero for negativo

count = result = 0

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print('FIM')
        break
    print('-' * 20)
    while count < 10:
        count += 1
        result = num * count
        print(f'{num} x {count:2} = {result}')
    count = 0
    print('-' * 20)
