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


if __name__ == "__main__":
    extra = True
    while True:
        mode = input("Enter mode: C/D/B (Code/Decode/Bye): ")
        if mode.lower() == "c":
            text = input("Enter text: ")
            coded = code(text, extra)
            print("\nCoded: {}{}{}".format(colored(text="[", color="red"), coded, colored(text="]", color="red")))
            print("\nDecoded: {}{}{}".format(colored(text="[", color="red"), decode(coded, extra), colored(text="]", color="red")))
        elif mode.lower() == "d":
            print("Decoded: {}{}{}".format(colored(text="[", color="red"), decode(input("Text: "), extra), colored(text="]", color="red")))
        elif mode.lower() == "b":
            break
# decodeText = input("Decode: ")
# print(decode(decodeText, extra=True))