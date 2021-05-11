def area(base, height):
    a = base*height/2
    print(f'The area of your triangle is {a}')

def trigle_type(base, height):
    h = (base**2 * height**2)**0.5
    if base == height == h:
        print('Your triangle is equilateral.')
    elif base == height:
        print('Your triangle is isosceles.')
    else:
        print('Your triangle is scalene.')

if __name__ == '__main__':
    b = float(input('Enter the base: '))
    h = float(input('Enter the height: '))
    area(b, h)
    trigle_type(b, h)