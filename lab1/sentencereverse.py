import re


def recursive_reverse_sentence(sentence: str):
    first_space_pos = sentence.find(' ')
    if first_space_pos >= 0:
        return recursive_reverse_sentence(sentence[first_space_pos + 1:]) + ' ' + sentence[:first_space_pos]
    else:
        return sentence


def recursive_reverse_sentence_re(sentence: str):
    regex = re.compile(r'\b(\w+)\b[\s,.?!\'"]*')
    matches = list(regex.finditer(sentence))
    first_match, last_match = matches[0], matches[-1]

    fs, fe = first_match.span(1)
    ls, le = last_match.span(1)
    if first_match is None or last_match is None or first_match == last_match:
        return sentence
    else:
        return sentence[:fs] + last_match.group(1) \
               + recursive_reverse_sentence(sentence[fe:ls]) \
               + first_match.group(1) + sentence[le:]
