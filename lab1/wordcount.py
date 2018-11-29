def recursive_count_word(text: str, word):
    first_position = text.find(word)
    if first_position < 0:
        return 0
    else:
        return 1 + recursive_count_word(text[first_position + 1:], word)
