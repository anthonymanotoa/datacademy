import math

def cylinder(radius, height):
    base = math.pi * radius ** 2
    volume = round(base * height, 2)
    return f'The volume of your cylinder is {volume}'


def cube(length):
    volume = round(lenght ** 3, 2)
    return f'The volume of your cube is {volume}'


def pyramid(length_base, height):
    base = lenght_base ** 2
    volume = round(base * height / 3, 2)
    return f'The volume of your pyramid is {volume}'


if __name__ == '__main__':
    type_shape = int(input('''
    Choose a 3d shape:
    [1] Cylinder
    [2] Cube
    [3] Pyramid
    '''))

    if type_shape == 1:
        radius = float(input('Enter the radius of the cylinder: '))
        height = float(input('Enter the height of the cylinder: '))
        print(cylinder(radius, height))
    elif type_shape == 2:
        lenght = float(input('Enter de lenght of the cube: '))
        print(cube(lenght))
    elif type_shape == 3:
        height = float(input('Enter the heigth of the pyramid: '))        
        lenght_base = float(input('Enter the length of the base: '))
        print(pyramid(lenght_base, height))