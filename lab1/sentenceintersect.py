import re


regex = re.compile(r'\b(\w+)\b[\s,.?!\'"]*')


def recursive_sentence_intersect(sent1: str, sent2: str):
    first_word_match1 = regex.search(sent1)
    first_word_match2 = regex.search(sent2)
    if not first_word_match1 or not first_word_match2:
        return False
    return \
        first_word_match1.group(1) == first_word_match2.group(1) \
        or recursive_sentence_intersect(sent1[first_word_match1.end(0):], sent2) \
        or recursive_sentence_intersect(sent1, sent2[first_word_match2.end(0):])
