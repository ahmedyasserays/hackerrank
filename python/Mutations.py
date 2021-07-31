def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]