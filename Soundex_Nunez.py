"""
Soundex System Coding
by: Johnny Nunez

This is a small program to demonstrate Soundex and save results to files.
Soundex is a system that encodes a word into a letter followed by three
numbers that roughly describe how the word sounds. Therefore, similar sounding words
have the same four-character code.

Simply enter your input when prompted and, it will be converted automatically.
Enter 0 to escape the main loop of the program.
"""
import os


def main():
    splash()

    name = input("Enter your name: ")

    soundex_name = convert(name)

    conversions = {}
    conversions.update({name: soundex_name})

    print("Hello {}! Welcome to the Soundex System.".format(soundex_name))
    conversions = loop(conversions)

    save_prompt = input("Do you wish to save?(y/n): ")
    if save_prompt == "y" or save_prompt == "Y":
        file(conversions)
    else:
        print("Program terminated")


def splash():
    # ASCII art splash
    print("   _____ ____  __  ___   ______  _______  __")
    print("  / ___// __ \/ / / / | / / __ \/ ____/ |/ /")
    print("  \__ \/ / / / / / /  |/ / / / / __/  |   / ")
    print(" ___/ / /_/ / /_/ / /|  / /_/ / /___ /   |  ")
    print("/____/\____/\____/_/ |_/_____/_____//_/|_|  ")
    print('\n')


def convert(user_input):
    user_input = user_input.upper()
    checks = \
        [
            # 1
            ['B', 'F', 'P', 'V'],
            # 2
            ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'],
            # 3
            ['D', 'T'],
            # 4
            ['L'],
            # 5
            ['M', 'N'],
            # 6
            ['R']
        ]

    # stores the soundex code as a list for easier manipulation
    s_code = [user_input[0]]

    # Go through each letter in the string and convert it besides the first
    for letter in user_input[1:]:
        for index in range(1, 6):
            if letter in checks[index - 1]:
                s_code.append(str(index))

    s_code = clean(s_code)

    # take the data generated from user input and join the values to create a string
    soundex_word = ''.join(s_code)

    return soundex_word


def clean(code):
    if code.__len__() < 4:
        while code.__len__() < 4:
            code.append('0')

    return code


def file(data):
    file_name = input("Enter name for save file: ")
    file_name += ".txt"
    directory = os.path.dirname(__file__)
    save_data = open(os.path.join(directory, 'Data', file_name), "w")

    for word in data:
        save_data.write(word + " : " + data[word] + '\n')

    save_data.close()

    print("File saved")


def loop(data, word=''):
    if word == '0':
        return data
    print("If you wish to quit, enter 0")

    word = input("\nEnter a word to convert: ")
    while word != '0':
        soundex_word = convert(word)
        data.update({word: soundex_word})
        print(word.upper() + " : " + soundex_word)
        loop(data, word)
        return data

    return data


# this makes sure we're using the tool directly, instead of using it as an import
if __name__ == "__main__":
    main()

'''
OUTPUT

Johnny : J550
Cat : C300
Dog : D200
Salamander : S4553
Frog : F200
Fish : F200

..\Data\animals.txt
'''