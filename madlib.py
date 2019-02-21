"""
Console app that generates MadLib from text file + user input
"""
import re


def madlib(usr_inp=[]):
    """ Console app that generates MadLib from text file + user input """
    print('** This is a CLI MadLib app; for each prompt below, enter a value of your choice **')
    text = ''
    words = []
    with open('assets/madlib_text', 'r') as file:
        for line in file:
            text += line
            words += re.findall(r"{[a-zA-Z0-9 '-]*}", line)
    if usr_inp == []:
        for word in words:
            word_prompt = re.sub(r"[{}]", '', word)
            usr_inp.append(input('Enter a value for ' + word_prompt + ': '))
    for word in usr_inp:
        text = re.sub(r"{[a-zA-Z0-9 '-]*}", word, text, 1)
    with open('assets/updated_madlib_text', 'w') as file:
        file.write(text)
    print(text)
    return text

if __name__ == '__main__':
    madlib()
