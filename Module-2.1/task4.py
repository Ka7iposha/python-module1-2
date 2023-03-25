def join(separator, sequence_of_strings):
    k = ''
    for i in range(len(sequence_of_strings)):
        result = sequence_of_strings[i] + separator
        k += result
    k = k[:-1]
    return k


def print_to_string(*items, sep=' ', end='\n'):
    a = join(sep, items)
    return a + end


