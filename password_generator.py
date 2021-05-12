# This is a bonus project

import string
import random

def pass_gen(long, pass_type):

    if pass_type == 1:
        characters = list(string.ascii_letters)
    elif pass_type == 2:
        characters = list(string.ascii_letters) + list(string.ascii_uppercase)
    elif pass_type == 3:
        characters = list(string.ascii_letters) + list(string.ascii_uppercase) + list(string.digits)
    elif pass_type == 4:
        characters = list(string.ascii_letters) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation)
        characters.append(' ')

    password = ''
    for _ in range(long):
        password += random.choice(characters)
    
    return password

if __name__ == '__main__':
    long = int(input('How long will your password be? (number) '))
    pass_type = int(input('''Choose an option:
    [1] Lower letters
    [2] Lower and upper letters
    [3] Option 2 + numbers
    [4] Option 3 + special characters
Option number '''))
    print('\n' + 'Your new password is:')
    print(pass_gen(long, pass_type))