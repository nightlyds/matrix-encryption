# The most interesting part
def characters_keys(language_array, language_name):
    # Object with characters and their keys
    language_with_keys = {}

    index = 0

    # For first part of the Array
    for i in language_array:
        # The first character`s key is length of the language word
        if(i == language_array[0]):
            language_with_keys[i] = len(language_name)
        
        # Next characters has keys by the formula: previus key * 2 + 1
        else:
            language_with_keys[i] = language_with_keys[language_array[index - 1]] * 2 + 1

        index += 1

        # Check the middle of the Array
        if index >= round(len(language_array) / 2):
            break

    # The same for cicle, but for the second part of the Array
    for i in range(index, len(language_array)):
        if(language_array[i] == language_array[round(len(language_array) / 2)]):
            language_with_keys[language_array[i]] = len(language_name) + 1
        else:
            language_with_keys[language_array[i]
                               ] = language_with_keys[language_array[index - 1]] * 2 + 1

        index += 1

    # Return ready object with characters and their keys
    return language_with_keys
