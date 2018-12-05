import re


def recursive_substring(string, position, length):
    if position >= len(string) or position < 0:
        raise ValueError('Wrong position argument!')
    if position + length > len(string):
        raise ValueError('Wrong length argument')
    current_char = string[position]
    if length <= 1:
        return current_char
    else:
        return current_char + recursive_substring(string, position + 1, length - 1)
    pass


def recursive_count_word(text: str, word):
    first_position = text.find(word)
    if first_position < 0:
        return 0
    else:
        return 1 + recursive_count_word(text[first_position + 1:], word)


def recursive_word_match(sentence: str, word: str):
    regex = re.compile(r'\b' + word + r'\b')
    match = regex.search(sentence)
    if match:
        end = match.end()
        return 1 + recursive_word_match(sentence[end:], word)
    else:
        return 0


def recursive_find_word(sentence: str, word: str):
    regex = re.compile(r'\b(\w+)\b')
    word_match = regex.search(sentence)
    if not word_match:
        return False
    if word is None:
        exact_word_regex = re.compile(r'\b' + word_match.group(1) + r'\b')
        exact_word_match = exact_word_regex.search(sentence[word_match.end() + 1:])
        word = None if not exact_word_match else exact_word_match.group(0)
    return True if word_match.group(1) == word else recursive_find_word(sentence[word_match.end():], word)


def recursive_word_replace(text: str, word_to_find: str, word_to_replace: str):
    start = text.find(word_to_find)
    if start >= 0:
        return text[:start] + \
               word_to_replace + \
               recursive_word_replace(text[start + len(word_to_find):], word_to_find, word_to_replace)
    else:
        return text


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


def recursive_sentence_intersect(sent1: str, sent2: str):
    regex = re.compile(r'\b(\w+)\b[\s,.?!\'"]*')
    first_word_match1 = regex.search(sent1)
    first_word_match2 = regex.search(sent2)
    if not first_word_match1 or not first_word_match2:
        return False
    return \
        first_word_match1.group(1) == first_word_match2.group(1) \
        or recursive_sentence_intersect(sent1[first_word_match1.end(0):], sent2) \
        or recursive_sentence_intersect(sent1, sent2[first_word_match2.end(0):])


def recursive_word_length(string: str):
    return (1 if re.match(r'\w', string[0]) else 0) + recursive_word_length(string[1:]) if len(string) > 0 else 0


def recursive_word_swap(sentence: str, first_word_idx=0, last_word_idx=0):
    last_word_start = sentence.rfind(' ') + 1
    first_word_pos, last_word_pos = first_word_idx, last_word_start + last_word_idx
    fw_char = sentence[first_word_pos]
    lw_char = sentence[last_word_pos] if last_word_pos < len(sentence) else ''

    regex = re.compile(r'\w')
    first_valid, last_valid = regex.match(fw_char), regex.match(lw_char)

    if not first_valid and not last_valid:
        return sentence

    f_swap_part, l_swap_part = '', ''
    if first_valid:
        l_swap_part = fw_char
        first_word_idx += 1
    if last_valid:
        f_swap_part = lw_char
        last_word_idx += 1
    return recursive_word_swap(
        sentence[:first_word_pos]
        + f_swap_part
        + sentence[first_word_pos + 1:last_word_pos]
        + l_swap_part
        + sentence[last_word_pos + 1:],
        first_word_idx,
        last_word_idx
    )


def test_substr():
    print('Substring')

    string = '1234567'
    start_position = 2
    length = 4
    print(f'String: "{string}"\nStart position: {start_position}\nLength: {length}')

    result = recursive_substring(string, start_position, length)
    print(result)

    print()


def test_word_count():
    print('Word count')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    print(f'Sentence: "{sentence}"\nWord: "{word}"')

    result = recursive_count_word(sentence, word)
    print(result)

    print()


def test_word_match():
    print('Word match')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    print(f'Sentence: "{sentence}"\nWord: "{word}"')

    result = recursive_word_match(sentence, word)
    print(result)

    print()


def test_word_find():
    print('Word find')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    print(f'Sentence: "{sentence}"\nWord: "{word}"')

    result = recursive_find_word(sentence, word)
    print(result)

    print()


def test_word_replace():
    print('Word replace')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    replacement = '123'
    print(f'Sentence: "{sentence}"\nWord: "{word}"\nReplacement: "{replacement}"')

    result = recursive_word_replace(sentence, word, replacement)
    print(result)

    print()


def test_sentence_reverse():
    print('Sentence reverse')

    sentence = 'Hello world, world hello, world.'

    print(f'Sentence: "{sentence}"')

    result = recursive_reverse_sentence_re(sentence)
    print(result)

    print()


def test_sentence_intersect():
    print('Sentence intersect')

    sentence1 = 'Hello world, world hello, world.'
    sentence2 = 'Hi world!'

    print(f'Sentence 1: "{sentence1}"\nSentence 2: "{sentence2}"')

    result = recursive_sentence_intersect(sentence1, sentence2)
    print(result)

    print()


def test_word_length():
    print('Word length')

    word = '  world!  '

    print(f'Word: "{word}"')

    result = recursive_word_length(word)
    print(result)

    print()


def test_word_swap():
    print('Swap first and last words')

    sentence = 'Hello world, world hello, world'

    print(f'Sentence: "{sentence}"')

    result = recursive_word_swap(sentence)
    print(result)

    print()


def main():
    test_substr()
    test_word_count()
    test_word_match()
    test_word_find()
    test_word_replace()
    test_sentence_reverse()
    test_sentence_intersect()
    test_word_length()
    test_word_swap()


if __name__ == '__main__':
    main()
