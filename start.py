from decryptor import decryptor
from encryptor import encryptor
from characters_keys import characters_keys
from introduce import introduce, printCharacters
from answer import answer

# Return: Matrix or Number type | True or False
encryption_type = introduce()

# The array for the language
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# For standart I set English, but you can also add condition for other languages and arrays with their alphabet
language_name = 'English'

# Get ready encrypted object with characters from the Array above and their keys
language_with_keys = characters_keys(english, language_name)

print('\n')
print(" Do u want encrypt or decrypt: ".center(61, '='))
print('\n')
print('1. Encrypt'.center(22))
print('\n')
print('2. Decrypt'.center(22))
print('\n')
print('3. Exit'.center(20))
print('\n')
printCharacters('=', 62)
print('\n')

# Return: Encrypt or Descrypt | True or False
encrypt = answer(printCharacters)

# Decrypt by the Matrix method
if(encryption_type == True and encrypt == False):
    # Return: string with decrypted characters
    print(decryptor("MATRIX", language_with_keys))

# Decrypt by the Number method
elif(encryption_type == False and encrypt == False):
    print(decryptor("NUMBER", language_with_keys))

# Encrypt by the Matrix method
elif(encryption_type == True and encrypt == True):
    print(encryptor("MATRIX", None))

# Encrypt by the Number method
elif(encryption_type == False and encrypt == True):
    print(encryptor("NUMBER", language_with_keys))

else:
    quit()
