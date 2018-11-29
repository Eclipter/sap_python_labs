import re


def recursive_find_word(sentence: str, word: str):
    regex = re.compile(r'\b(\w+)\b[\s,.?!\'"]*')
    match = regex.match(sentence)
    if match:
        return match.group(1) == word or recursive_find_word(sentence[match.end():], word)
    else:
        return False
