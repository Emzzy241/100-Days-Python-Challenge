# Each string in the list is one row of the ASCII art.
# Raw strings (r"...") let backslashes print literally.

logo = [
    r" ,******,                                                    ",
    r"|A_    _.|      _     _             _      _             _   ",
    r"|K V )...|     | |__ | | __ _  __  | |__  (_) __ _  __  | |__",
    r"|\ /|K /\|     | '_ \| |/ _` |/ _| | / /  | |/ _` |/ _| | / /",
    r"| V |/ \ |     |_.__/|_|\__,_|\__| |_\_\ _/ |\__,_|\__| |_\_\ ",
    r"'....|\ / |                             |__/                 ",
    r"     | V K|                                                  ",
    r"     '****'                                                  ",
]

for line in logo:
    print(line)