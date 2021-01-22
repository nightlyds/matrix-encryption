import time
from answer import answer


# Print some character some time
def printCharacters(characters, amount):
    for i in range(1, amount):
        time.sleep(.02)
        print(characters, end='')


def introduce():

    printCharacters('=', 62)
    print('\n')
    print('你好, 我是矩阵加密'.center(54))
    print('HELLO, I AM MATRIX ENCRYPTION!'.center(61))
    printCharacters('=', 62)
    print('\n')

    print(' Choose option: '.center(61, '='))
    print('\n')
    print('1. Matrix enctryption (complex)'.center(44))
    print('\n')
    print('2. Numbers encryption'.center(34))
    print('\n')
    print('3. Exit'.center(20))
    print('\n')
    printCharacters('=', 62)
    print('\n')
    
    introduce_answer = answer(printCharacters)

    if(introduce_answer == True):
        return True
    elif (introduce_answer == False):
        return False
    else:
        quit()