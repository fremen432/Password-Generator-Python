"""
inputs (radios):
    include upper-case characters? [Y/N]
    include lower-case characters? [Y/N]
    include numbers? [Y/N]
    include special characters? [Y/N]
    password character length? [int] ( min: 6, max: 25, default: 10 )
    included key word? [str]

output (string):
    single password (option to copy)
"""

import random

CHAR_UPPER = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

CHAR_LOWER = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

CHAR_SPECIAL = [
    "~",
    "`",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    "{",
    "}",
    "[",
    "]",
    "|",
    "\\",
    "/",
    ":",
    ";",
    '"',
    "'",
    "<",
    ">",
    ",",
    ".",
    "?",
]

CHAR_NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

MIN_password_length = 6
MAX_password_length = 30


def generate_password(
    include_upper,
    include_lower,
    include_numbers,
    include_special,
    password_length,
    key_word,
):
    if password_length > MAX_password_length:
        return f"Password must be no longer than {MAX_password_length} characters."
    if password_length < MIN_password_length:
        return f"Password must be no shorter than {MIN_password_length} characters."

    if len(key_word) == password_length:
        return key_word

    if len(key_word) > password_length:
        return f"The key word you've chosen has more than the maximum character limit at: {password_length} characters.\nPlease choose a shorter key word."

    CHAR_POOL = []
    PASSWORD_LIST = []

    if include_upper:
        CHAR_POOL += CHAR_UPPER
    if include_lower:
        CHAR_POOL += CHAR_LOWER
    if include_numbers:
        CHAR_POOL += CHAR_NUMBERS
    if include_special:
        CHAR_POOL += CHAR_SPECIAL

    # scramble char pool list for more random characters
    random.shuffle(CHAR_POOL)

    # picking random characters from CHAR_POOL and putting them in PASSWORD_LIST
    for x in range(password_length):
        random_number = random.randrange(0, password_length)
        PASSWORD_LIST.append(CHAR_POOL[random_number - 1])

    if key_word:
        # return key_word
        # what is difference between length of PASSWORD_LIST and key_word
        # this will give max index of key_word placement in PASSWORD_LIST
        diff = len(PASSWORD_LIST) - len(key_word)  # 21

        # randomly picked index of first char of keyWord in PASSWORD LIST
        i = random.randrange(0, diff)

        # insert key_word at i index in PASSWORD_LIST, then remove excess characters so FULL_PASSWORD length matches password_length inputted by user
        PASSWORD_LIST.insert(i, key_word)
        for x in range(len(key_word)):
            PASSWORD_LIST.pop(-1)

    FULL_PASSWORD = "".join(PASSWORD_LIST)
    return FULL_PASSWORD


# res_01 = generate_password(True, False, True, False, 10, "yo")
# res_02 = generate_password(True, True, True, False, 10, "yo")
# res_03 = generate_password(True, False, True, True, 10, "yo")
res_04 = generate_password(True, True, True, True, 7, "buurp")

print(res_04)
