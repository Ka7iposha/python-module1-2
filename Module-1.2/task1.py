animals = [
    ['курочка', 'курочку', '{animal} по зёрнышку кудах-тах-тах'],
    ['уточка', 'уточку', '{animal} та-ти-та-та'],
    ['индюшонок', 'индюшонка', '{animal} фалды-балды'],
    ['кисуня', 'кисоньку', '{animal} мяу-мяу'],
    ['собачонка', 'собачонку', '{animal} гав-гав'],
    ['коровёнка', 'коровёнку', '{animal} муки-муки'],
    ['поросёнок', 'поросёнка', '{animal} хрюки-хрюки'],
    ['телевизор', 'телевизор', '{animal} надо, надо, ведь у нас такое стадо']
]

first = 0
second = 1
third = 2
repetitions = 2
transfer = '\n'
ask = 'Бабушка, бабушка, купим {animal}!'


# функция генерирующая 1 часть куплетов песни
def question(animal_a, times):
    result = ''
    line = ask.format(animal=animals[animal_a][second])
    for i in range(0, times):
        result += line + transfer
    return result


# функция содержащая длинну списка
def ending(length):
    return length == len(animals) - 1


# функция, меняющая строчные буквы на заглавные в начале строки
def capital_letters(word, phrase):
    return phrase if phrase.find(word) \
        else phrase.replace(word, word.title())


# функция, генерирующая вторую часть куплета
def after_question(number_animal):
    result = ''
    for i in reversed(range(0, number_animal + 1)):
        sound_animals = animals[i][third].format(animal=animals[i][first])
        sound_animals = capital_letters(animals[i][first], sound_animals)
        result += sound_animals
        if ending(i):
            result += '!'
            break
        result += (',' + transfer) if i else ('.' + transfer)
    return result


# функция генерирующая весь текст
def song_result():
    result = ''

    for i in range(0, len(animals)):
        result += question(i, repetitions)
        result += after_question(i)
        result += transfer
    return result


print(song_result())

