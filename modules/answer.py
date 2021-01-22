def answer(printCharacters):
    # Check on the correct answer and return value of the encryption type
    while True:
        try:
            introduce_answer = input("Type your answer: ")

            if(introduce_answer == '1'):
                return True

            elif(introduce_answer == '2'):
                return False

            elif(introduce_answer == '3'):
                print('\n')
                printCharacters('=', 62)
                print('\n')
                print('SEE YOU!'.center(62))
                printCharacters('=', 62)
                print('\n')
                break
            else:
                print('\n')
                print('! TYPE A CORRECT ANSWER !'.center(62, '='))
                print('\n')

        except ValueError:
            print('You caught the error :(')
