# Write code below 💖
import math

print('==================')
print('Area Calculator 📐')
print('==================')
print('')
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
print('')

contador = 9
while (contador == 9):
    a = int(input('Which shape:'))

    if a == 1:
        height = float(input('Height:'))
        base = float(input('Base:'))

        area = (height * base) / 2

        print('Area:', area)

    elif a == 2:
        width = float(input('Width:'))
        length = float(input('Length:'))

        area = length * width

        print('Area:', area)

    elif a == 3:
        side = float(input('Side:'))

        area = side * side

        print('Area:', area)

    elif a == 4:
        radius = float(input('Radius:'))

        area = math.pi * (radius * radius)

        print('Area:', area)

    elif a == 5:

        print('Bye')
        break

    else:
        print("that option is not available")
        contador = 9