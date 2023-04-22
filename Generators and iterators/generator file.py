import codecs

handle = codecs.open(r"C:\Users\mastermor\Desktop\text.txt", "r", "utf_8_sig")


def gtext(n):
    while True:
        data = handle.read(n)
        yield data

        if not data:
            break


for i in gtext(1024):
    print("____________________")
    print(i)