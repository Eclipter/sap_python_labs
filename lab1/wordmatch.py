import re


def recursive_count_matched_words(sentence: str, word: str):
    regex = re.compile(r'\b' + word + r'\b')
    match = regex.search(sentence)
    if match:
        end = match.end()
        return 1 + recursive_count_matched_words(sentence[end:], word)
    else:
        return 0
