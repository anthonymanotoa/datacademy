def ranges(x, y, z):
    if x < z < y:
        print(f'Your lucky number is {int(z)}')
    else:
        print(f'Your number is {int(z)}')
        z = float(input('Try another number: '))
        ranges(x, y, z)


if __name__ == '__main__':
    x = float(input('Enter a number: '))
    y = float(input('Enter another number (higher): '))
    z = float(input('Enter one more: '))
    ranges(x, y, z)