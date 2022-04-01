from numpy import ceil
from termcolor import colored

import os
os.system("color")


def code(text : str, extra=False):
    output = ""
    if len(text) != 1:
        for char in range(len(text)):
            if char % 2 == 0: output += text[char]

        for char in range(1, len(text)):
            if char % 2 != 0: output += text[char]
        
        output=''.join(reversed(output)) if extra else output
    else: output = text
    return output


def decode(text : str, extra=False):
    output = ""
    if len(text) != 1:
        reversED = ''.join(reversed(text)) if extra else text

        for char in range(int(ceil(len(reversED) / 2))):
            output += reversED[char]
        
        index = 1
        output_list = list(output)
        for char in range(int(ceil(len(reversED) / 2)), len(reversED)):
            output_list.insert(index, reversED[char])
            index += 2

        output = "".join(output_list)
    else: output = text
    return output

# print("Decoded: {}".format(decode(input("Text: "), True)))
text = input("Enter text: ")
coded = code(text, True)
print("Coded: {}{}{}".format(colored(text="[", color="red"), coded, colored(text="]", color="red")))
print("Decoded: {}{}{}".format(colored(text="[", color="red"), decode(coded, True), colored(text="]", color="red")))

# decodeText = input("Decode: ")
# print(decode(decodeText, extra=True))