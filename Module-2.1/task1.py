def ljust(string, width, underline):
    return string + underline * (width - len(string))


def rjust(string, width, underline):
    return underline * (width - len(string)) + string


def center(string, width, underline):
    if (width - len(string)) % 2 == 0:
        left_border = int(((width - len(string)) / 2))
        right_border = left_border
    else:
        left_border = int(((width - len(string)) / 2))
        right_border = int(((width - len(string)) / 2) + 1)
    return underline * left_border + string + underline * right_border


n = 'hello'
fill = '==>'
b = 8

print(ljust(n, b, fill))

