import numpy as np
from modules.answer import answer
from modules.introduce import printCharacters


def decryptor(encryption_type, language_with_keys):
    # The array for decrypted characters
    decrypted_text = []

    def checkForAdditionalCharacters(decryptionFunction):
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
                decryptionFunction()

            # Return: the Transformed Array to the string
            else:
                return " ".join(decrypted_text)

    def searchCharacterByTheKey(value):
        # Looking for keys in Object with character:key and add them to the Decrtypted Array
        for key, character in language_with_keys.items():
            if(value == character):
                decrypted_text.append(key)

    if(encryption_type == "MATRIX"):
        # The function uses for creating matrixies and calculate their determinant and add encrypted character to the Array with them
        def decryptorMatrix():
            print('\n')

            # Check for the correct answer
            while(True):
                try:
                    # Rows of the Matrix
                    rows = int(input("Type the number of rows: "))

                    # Columns of the Matrix
                    columns = int(input('Type the number of columns: '))

                    if(rows >= 0 and columns >= 0):
                        break

                except ValueError:
                    print('You caught the error :(')

            while True:
                try:
                    print('\n')
                    print('Type the entries in a single line (separated by space): ')
                    print('\n')

                    # Transform numbers from the input to the Array
                    entries = list(map(int, input().split()))

                    if(len(entries) == rows * columns):
                        break

                except ValueError:
                    print('You caught the error :(')

            # Transform the Array to the Matrix
            matrix = np.array(entries).reshape(rows, columns)

            # Calculate a determinant of the Matrix
            determinant = round(np.linalg.det(matrix))

            print('\n')
            print(matrix)
            print('\n')

            # Call search with the determinant value
            searchCharacterByTheKey(determinant)

        # Call once function by default
        decryptorMatrix()

        # Call the check function with function for decryption matrix in attribute and return that value
        return checkForAdditionalCharacters(decryptorMatrix)

    elif (encryption_type == "NUMBER"):
        print('\n')

        def decryptorNumber():
            # Check for the correct answer
            while(True):
                try:
                    # Rows of the Matrix
                    number = int(input("Type the number: "))

                    if(type(number) == int and number >= 0):
                        break

                except ValueError:
                    print('You caught the error :(')

            # Call search with the number value from the input
            searchCharacterByTheKey(number)

        # Call once function by default
        decryptorNumber()

        # Call the check function with function for decryption matrix in attribute and return that value
        return checkForAdditionalCharacters(decryptorNumber)
