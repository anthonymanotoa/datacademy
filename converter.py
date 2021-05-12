def converter(type_converter, unit):
    if type_converter == 1:
        miles = unit * 1.609344
        return f'{unit} kilometers are {miles} miles.'
    elif type_converter == 2:
        km = unit / 1.609344
        return f'{unit} miles are {km} kilometers.'


if __name__ == '__main__':
    type_converter = int(input('''
    Choose the option to convert:
    [1] Kilometers to miles
    [2] Miles to kilometers
    '''))
    unit = float(input('Enter the value: '))
    print(converter(type_converter, unit))