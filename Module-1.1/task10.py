number_dict = {
    1: 'one', 2: 'two', 3: 'three',
    4: 'four', 5: 'five',
    6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen',
    20: 'twenty ', 30: 'thirty ',
    40: 'forty ', 50: 'fifty ',
    60: 'sixty ', 70: 'seventy ',
    80: 'eighty ', 90: 'ninety '
}


def number_in_words(n):
    if 1 <= n <= 20 or n == 30 or n == 40 or n == 50 or n == 60 or n == 70 or n == 80 or n == 90:
        return number_dict[n]
    else:
        second = n % 10
        first = n - second
        return number_dict[first] + number_dict[second]


n = int(input())

print(number_in_words(n))
