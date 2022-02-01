import random

# characters
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['#', '%', '*']


def get_password(pw_nums:int, pw_small_lets:int, pw_big_lets:int, pw_syms:int):
    password_list = []

    while pw_nums > 0:
        password_list.append(random.choice(nums))
        pw_nums -= 1

    while pw_small_lets > 0:
        password_list.append(random.choice(small_letters))
        pw_small_lets -= 1

    while pw_big_lets > 0:
        password_list.append(random.choice(big_letters))
        pw_big_lets -= 1

    while pw_syms > 0:
        password_list.append(random.choice(symbols))
        pw_syms -= 1

    random.shuffle(password_list)
    return "".join(el for el in password_list)


# pw - password
while True:
    pw_len = int(input("How long should the generated password be?\n"))
    if 100 >= pw_len > 0:
        break
    print("Try again!")

# Get Proportions
pw_nums = round(pw_len / 3)
pw_small_lets = round((pw_len - pw_nums) / 2)
pw_big_lets = round(pw_small_lets / 2)
pw_syms = pw_len - (pw_nums + pw_small_lets + pw_big_lets)

# Password
password = get_password(pw_nums, pw_small_lets, pw_big_lets, pw_syms)

output = f'''
PASSWORD GENERATED
1. Size: {pw_len}
2. Numbers: {pw_nums}
3. Small Letters: {pw_small_lets}
4. Big Letters:  {pw_big_lets}
5. Symbols: {pw_syms}
6. Result: {password}
'''

print(output)