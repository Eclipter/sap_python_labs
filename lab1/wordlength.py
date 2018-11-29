import re


def recursive_word_length(string: str):
    return (1 if re.match(r'\w', string[0]) else 0) + recursive_word_length(string[1:]) if len(string) > 0 else 0
