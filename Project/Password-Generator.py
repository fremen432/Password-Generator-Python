from tkinter import *
import random
from Constants import (
    CHAR_LIST_UPPER,
    CHAR_LIST_LOWER,
    CHAR_LIST_SPECIAL,
    CHAR_LIST_NUMBERS,
    color_white,
    palette_01,
    palette_02,
    palette_03,
    palette_04,
    palette_05,
    MIN_password_length,
    MAX_password_length,
    DEFAULT_password_length,
)

root = Tk()
root.title("Password Generator")
root.geometry("500x500")
root.iconbitmap("Project/Key-Icon.ico")

include_upper = BooleanVar()
include_lower = BooleanVar()
include_numbers = BooleanVar()
include_special = BooleanVar()
password_length = IntVar()
key_word = StringVar()
selected = StringVar()
GENERATED_PASSWORD = StringVar()

include_upper.set(True)
include_lower.set(True)
include_numbers.set(True)
include_special.set(True)
password_length.set(DEFAULT_password_length)
key_word.set("")

label_padx = 1
label_pady = 5
label_borderwidth = 5
label_border = 10
label_width = 25


def generate_password(
    include_upper,
    include_lower,
    include_numbers,
    include_special,
    password_length,
    key_word,
):
    if password_length > MAX_password_length:
        return f"Password can be no longer than {MAX_password_length} characters."
    if password_length < MIN_password_length:
        return f"Password must have at least {MIN_password_length} characters."
    if len(key_word) == password_length:
        return key_word
    if len(key_word) > password_length:
        return f"The key word you've chosen has more than the maximum character limit at: {password_length} characters.\nPlease choose a shorter key word."

    CHAR_POOL = []
    PASSWORD_CHAR_LIST = []

    if include_upper:
        CHAR_POOL += CHAR_LIST_UPPER
    if include_lower:
        CHAR_POOL += CHAR_LIST_LOWER
    if include_numbers:
        CHAR_POOL += CHAR_LIST_NUMBERS
    if include_special:
        CHAR_POOL += CHAR_LIST_SPECIAL
    if len(CHAR_POOL) == 0:
        return "You must check at least 1 character class."

    # scramble char pool list for more random characters
    random.shuffle(CHAR_POOL)

    # picking random characters from CHAR_POOL and putting them in PASSWORD_CHAR_LIST
    for x in range(password_length):
        random_number = random.randrange(0, len(CHAR_POOL))
        PASSWORD_CHAR_LIST.append(CHAR_POOL[random_number])

    if key_word:
        # find difference between len(PASSWORD_CHAR_LIST) and len(key_word)
        # this will give max index of key_word placement in PASSWORD_CHAR_LIST
        diff = len(PASSWORD_CHAR_LIST) - len(key_word)

        # randomly picked index of first char of key_word in PASSWORD_CHAR_LIST
        i = random.randrange(0, diff)

        # insert key_word in PASSWORD_CHAR_LIST at index i
        PASSWORD_CHAR_LIST.insert(i, key_word)

        # remove excess characters from PASSWORD_CHAR_LIST so FULL_PASSWORD length matches password_length
        for x in range(len(key_word)):
            PASSWORD_CHAR_LIST.pop(-1)

    FULL_PASSWORD = "".join(PASSWORD_CHAR_LIST)
    return FULL_PASSWORD


def print_selected():
    print(
        f"include_upper: {include_upper.get()}\ninclude_lower: {include_lower.get()}\ninclude_numbers: {include_numbers.get()}\ninclude_special: {include_special.get()}\npassword_length: {password_length.get()}\nkey_word: {key_word.get()}"
    )


def run():
    res = generate_password(
        include_upper.get(),
        include_lower.get(),
        include_numbers.get(),
        include_special.get(),
        password_length.get(),
        key_word.get(),
    )
    GENERATED_PASSWORD.set(res)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(GENERATED_PASSWORD.get())


# Initialize elements
CANVAS_root = Canvas(root, height=5000, width=5000, bg=palette_01)
CANVAS_root.place(relwidth=1, relheight=1, relx=0, rely=0)

FRAME_widgets = Frame(root, bg=palette_02)
FRAME_widgets.columnconfigure(0, weight=1)
FRAME_widgets.columnconfigure(1, weight=1)

LABEL_Title = Label(
    root,
    width=label_width,
    text="Password Generator",
    bg=palette_05,
    pady=10,
    font=(
        "",
        20,
    ),
)
LABEL_include_upper = Label(
    FRAME_widgets,
    width=label_width,
    text="Include upper-case characters: ",
    bg=palette_05,
    anchor=W,
    pady=label_pady,
)
LABEL_include_lower = Label(
    FRAME_widgets,
    width=label_width,
    text="Include lower-case characters: ",
    bg=palette_05,
    anchor=W,
    pady=label_pady,
)
LABEL_include_numbers = Label(
    FRAME_widgets,
    width=label_width,
    text="Include number characters: ",
    bg=palette_05,
    anchor=W,
    pady=label_pady,
)
LABEL_include_special = Label(
    FRAME_widgets,
    width=label_width,
    text="Include special characters: ",
    bg=palette_05,
    anchor=W,
    pady=label_pady,
)
LABEL_input_key_word = Label(
    FRAME_widgets,
    width=label_width,
    text="Include a key word: ",
    bg=palette_05,
    anchor=W,
    pady=label_pady,
)
LABEL_input_charLength = Label(
    FRAME_widgets,
    width=label_width,
    text="Password character length: ",
    bg=palette_05,
    anchor=W,
    pady=label_pady,
)

CHECK_include_upper = Checkbutton(
    FRAME_widgets,
    variable=include_upper,
    onvalue=1,
    offvalue=0,
    bg=palette_05,
)
CHECK_include_lower = Checkbutton(
    FRAME_widgets,
    variable=include_lower,
    onvalue=1,
    offvalue=0,
    bg=palette_05,
)
CHECK_include_numbers = Checkbutton(
    FRAME_widgets,
    variable=include_numbers,
    onvalue=1,
    offvalue=0,
    bg=palette_05,
)
CHECK_include_special = Checkbutton(
    FRAME_widgets,
    variable=include_special,
    onvalue=1,
    offvalue=0,
    bg=palette_05,
)

ENTRY_key_word = Entry(
    FRAME_widgets, width=25, bg=color_white, textvariable=key_word, border=label_pady
)

BTN_generate_password = Button(FRAME_widgets, text="Generate Password", command=run)
BTN_copy_to_clipboard = Button(
    FRAME_widgets, text="Copy to clipboard", command=copy_to_clipboard
)

SCALE_password_length = Scale(
    FRAME_widgets,
    orient=HORIZONTAL,
    from_=6,
    to=50,
    variable=password_length,
    length=150,
    bg=palette_05,
)

LABEL_GENERATED_PASSWORD = Label(
    FRAME_widgets, width=50, textvariable=GENERATED_PASSWORD, bg=color_white
)


# Placing elements in app
LABEL_include_upper.grid(row=0, column=0, pady=label_pady, padx=label_padx)
LABEL_include_lower.grid(row=1, column=0, pady=label_pady, padx=label_padx)
LABEL_include_numbers.grid(row=2, column=0, pady=label_pady, padx=label_padx)
LABEL_include_special.grid(row=3, column=0, pady=label_pady, padx=label_padx)
LABEL_input_key_word.grid(row=4, column=0, pady=label_pady, padx=label_padx)
LABEL_input_charLength.grid(row=5, column=0, pady=label_pady, padx=label_padx)

CHECK_include_upper.grid(row=0, column=1)
CHECK_include_lower.grid(row=1, column=1)
CHECK_include_numbers.grid(row=2, column=1)
CHECK_include_special.grid(row=3, column=1)

ENTRY_key_word.grid(row=4, column=1)
SCALE_password_length.grid(row=5, column=1)
LABEL_GENERATED_PASSWORD.grid(
    row=7, column=0, columnspan=2, pady=label_pady, padx=label_padx
)
BTN_generate_password.grid(row=8, column=0)
BTN_copy_to_clipboard.grid(row=8, column=1)

# LABEL_Title.place(anchor=CENTER, relx=0.5, rely=0.10)
# FRAME_widgets.place(anchor=CENTER, relx=0.5, rely=0.5)

# pack each parent widget to the root
LABEL_Title.pack(anchor=CENTER, pady=20)
FRAME_widgets.pack(anchor=CENTER)

root.mainloop()
