import numpy as np
from modules.answer import answer
from modules.introduce import printCharacters


def encryptor(encryption_type, language_with_keys):
    englishWithMatrices = [{'a': [[2, 1],
                                   [7, 7]]},
                            {'b': [[16, 1],
                                   [1, 1]]},
                            {'c': [[31, 1],
                                   [31, 2]]},
                            {'d': [[1, 1],
                                   [17, 80]]},
                            {'e': [[2, 1],
                                   [127, 127]]},
                            {'f': [[1, 2],
                                   [45, 345]]},
                            {'g': [[2, 1],
                                   [511, 511]]},
                            {'h': [[1, 2],
                                   [77, 1177]]},
                            {'i': [[2, 1],
                                   [2047, 2047]]},
                            {'j': [[1, 2],
                                   [5, 4105]]},
                            {'k': [[1, 1],
                                   [1, 8192]]},
                            {'l': [[2, 1],
                                   [16383, 16383]]},
                            {'m': [[1, 2],
                                   [233, 33233]]},
                            {'n': [[1, 1],
                                   [1, 9]]},
                            {'o': [[1, 2],
                                   [3, 23]]},
                            {'p': [[2, 1],
                                   [35, 35]]},
                            {'q': [[1, 2],
                                   [9, 89]]},
                            {'r': [[1, 1],
                                   [1, 144]]},
                            {'s': [[1, 2],
                                   [14, 315]]},
                            {'t': [[2, 1],
                                   [575, 575]]},
                            {'u': [[1, 1],
                                   [1, 1152]]},
                            {'v': [[2, 1],
                                   [2303, 2303]]},
                            {'w': [[4607, 1],
                                   [4607, 2]]},
                            {'x': [[1, 1],
                                   [1, 9216]]},
                            {'y': [[2, 1],
                                   [18431, 18431]]},
                            {'z': [[36863, 1],
                                   [36863, 2]]}]

    encrypted_characters = []

    def typeCharacters():
        # Check for the correct answer
        while True:
            try:
                print('\n')
                character_input = input('Type your character: ')
                print('\n')

                if(type(character_input) == str):
                    break

            except ValueError:
                print('You caught the error :(')

        # For the Matrix method search
        if(encryption_type == "MATRIX"):
            # Look at the Array with Matrices
            for i in englishWithMatrices:
                # Take key and character every object in the Array
                for key, character in i.items():
                    if(character_input == key):
                        # Add this character if it suits to the Encrypted Array
                        encrypted_characters.append(character)

        elif (encryption_type == "NUMBER"):
            # Look at the Array with Language keys and characters
            for key, character in language_with_keys.items():
                # Take key and character every object in the Array
                if(character_input == key):
                    # Add this character if it suits to the Encrypted Array
                    encrypted_characters.append(character)

    def checkForAdditionalCharacters():
        # Check for another matrix | number
        while True:
            print('\n')
            print(" Do u want type additinal characters?: ".center(61, "="))

            print('\n')
            print('1. Yes'.center(17))
            print('\n')
            print('2. No'.center(18))
            print('\n')
            print('3. Exit'.center(20))
            print('\n')
            printCharacters('=', 62)
            print('\n')

            # Return: True or False
            decryptor_answer = answer(printCharacters)

            if(decryptor_answer == True):
                typeCharacters()

            # Return: the Array with the encrypted characters
            else:
                return encrypted_characters

    # Call function by default
    typeCharacters()

    # Check for another character and return the Array with encrypted characters
    return checkForAdditionalCharacters()
