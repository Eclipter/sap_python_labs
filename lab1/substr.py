def recursive_substring(string, position, length):
    if position > len(string) or position < 0:
        raise ValueError('Wrong position argument!')
    if position + length > len(string):
        raise ValueError('Wrong length argument')
    current_char = string[position]
    if length <= 1:
        return current_char
    else:
        return current_char + recursive_substring(string, position + 1, length - 1)
    pass
