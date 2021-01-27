# MATRIX-ENCRTYPTION :trident:

### 你好 - HELLO!

Does everyone hear about different types of encryption? I do! Because of that I decided to write a new encryption type by myself. It's called: **MATRIX-ENCRYPTION**. If you ask me why it has that name, I will say you that: I wanted to make something linked with math and matrices were the first thing which I think about in that moment.

### LEARNING
The first stage of the encryption is a language alphabet and a language name, the first one is the object which will has some special characters in the future, the second one is for start point of these special characters.

You can open file [modules/characters_keys.py](https://github.com/nightlyds/matrix-encryption/blob/main/modules/characters_keys.py) and have a look at this algorithm. That`s just building object from the language alphabet with their unique characters (in this case: it is simple numbers). I was thinking about a binary tree algorithm, but I change my mind on another method that looks like [Algorithm](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/algorithm.jpg):

![ALGORITHM PHOTO](https://imageup.ru/img225/3701262/algorithm.jpg.html)

There are dividing alphabet on two parts, I will tell on English language example, the first one letter in the English alphabet is **'a'** and it have the special/unique character: **language_name.length** (for example, english word has the length: **7 characters** - that`s start point). The second letter will has special/unique character by the formula: **previus_character * 2 + 1** (for example: after **'a'** in the English alphabet is **'b'** letter and it will has: **7 * 2 + 1 = 8**), the full list looks like: [The Full Object With Keys And Characters](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/english_alphabet_with_characters.py)

The next stage is decryption. It works by the next method: you can choose **matrix method** or simpler method just typing **numbers**:
- **The Matrix Method** - You should type any size matrix, for example it can be **2x2, 3x3, 4x4** and etc matrices. A determinant of this matrix will be some number and that number is a special/unique character in [the Object with the English Alphabet and their special characters](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/english_alphabet_with_characters.py). If this determinant of the Matrix will the same like a character some letter in [The Object](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/english_alphabet_with_characters.py) it will add in the special **decrypted_characters** array.

- **The Number Method** - It works simpler than The Matrix Method, you don`t need use matrices, you can just use simple numbers, but you need know all special/unique characters for every letter in [The Object](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/english_alphabet_with_characters.py)

### If you don`t know what is matrix and determinant:
**Matrix** - is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns. [1](https://en.wikipedia.org/wiki/Matrix_(mathematics)). Matrix has any size, it can be **2x2, 3x3 of even 64x64** size. **The determinant** - in linear algebra, the determinant is a scalar value that can be computed from the elements of a square matrix and encodes certain properties of the linear transformation described by the matrix [2](https://en.wikipedia.org/wiki/Determinant). In our case you can use any size matrices, but you need know how to calculate the determinant of the matrix, if you choose The Matrix encryption method. That`s the formula [3](http://mozgan.ru/Images/Matrix/14.png):

![THE DETERMINANT OF MATRIX 3X3 FORMULA](http://mozgan.ru/Images/Matrix/14.png)

The encryption method. If you need encrypt some text, you can also choose the one option from the encryption methods. In depend from the method you will get matrices for your secret text or just numbers for every letter. [The Full Array Of The Matrices For Every Letter](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/english_alphabet_with_matrices.py)

These matrices is like example, you can change on any matrices which determinant is equal to the letter`s character in [The List With Letters And Characters](https://github.com/nightlyds/matrix-encryption/blob/main/learning_files/english_alphabet_with_characters.py)

## Installation

1. Use the package manager [pip](https://pypi.org/) to install packages.

2. Install the newest version of Python 3.

3. Install Numpy by the command:

```bash
pip3 install numpy
```
4. To start project type in the command line beigh in the project folder:

```bash
python3 start.py
```

## Techs

1. Python
    1. Numpy


## Contributing
Project is on development stage. It needs tests more clear code, more wide functionality and etc, beacuse of that pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Links

  - [Instagram](https://www.instagram.com/_daniels11/)
  - [Facebook](https://www.facebook.com/nightly.ds)
