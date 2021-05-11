import random

def rps(choose_1, choose_2):

    if human_choise not in options:
        print('Please pick a correct option.')
        return None

    if choose_1 == choose_2:
        print("It's a draw!")
    elif (choose_1 == 'rock' and choose_2 == 'scissors') or (choose_1 == 'scissors' and choose_2 == 'paper') or (choose_1 == 'paper' and choose_2 == 'rock'):
        print('*'*40 + '\n' + 'You win! 💚')
    else:
        print('*'*40 + '\n' + 'Laptop wins... 💔')


if __name__ == '__main__':
    options = ['rock', 'paper', 'scissors']
    print('''
    Choose between rock, paper and scissors.
    ''')
    human_choise = input(f'I choose... ').lower()
    laptop_choise = random.choice(options)
    print(f'Your laptop has choosen {laptop_choise}')
    rps(human_choise, laptop_choise)