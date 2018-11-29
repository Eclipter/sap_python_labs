def recursive_word_replace(text: str, word_to_find: str, word_to_replace: str):
    start = text.find(word_to_find)
    if start >= 0:
        return text[:start] + \
               word_to_replace + \
               recursive_word_replace(text[start + len(word_to_find):], word_to_find, word_to_replace)
    else:
        return text
