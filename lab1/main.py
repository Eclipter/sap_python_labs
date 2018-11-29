def test_substr():
    import substr
    print('Substring')

    string = '1234567'
    start_position = 2
    length = 4
    print(f'String: "{string}"\nStart position: {start_position}\nLength: {length}')

    result = substr.recursive_substring(string, start_position, length)
    print(result)

    print()


def test_wordcount():
    import wordcount
    print('Word count')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    print(f'Sentence: "{sentence}"\nWord: "{word}"')

    result = wordcount.recursive_count_word(sentence, word)
    print(result)

    print()


def test_wordmatch():
    import wordmatch
    print('Word match')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    print(f'Sentence: "{sentence}"\nWord: "{word}"')

    result = wordmatch.recursive_count_matched_words(sentence, word)
    print(result)

    print()


def test_wordfind():
    import wordfind
    print('Word find')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    print(f'Sentence: "{sentence}"\nWord: "{word}"')

    result = wordfind.recursive_find_word(sentence, word)
    print(result)

    print()


def test_wordreplace():
    import wordreplace
    print('Word replace')

    sentence = 'Hello world, world hello, world.'
    word = 'world'
    replacement = '123'
    print(f'Sentence: "{sentence}"\nWord: "{word}"\nReplacement: "{replacement}"')

    result = wordreplace.recursive_word_replace(sentence, word, replacement)
    print(result)

    print()


def test_sentencereverse():
    import sentencereverse
    print('Sentence reverse')

    sentence = 'Hello world, world hello, world.'

    print(f'Sentence: "{sentence}"')

    result = sentencereverse.recursive_reverse_sentence_re(sentence)
    print(result)

    print()


def test_sentenceintersect():
    import sentenceintersect
    print('Sentence intersect')

    sentence1 = 'Hello world, world hello, world.'
    sentence2 = 'Hi world!'

    print(f'Sentence 1: "{sentence1}"\nSentence 2: "{sentence2}"')

    result = sentenceintersect.recursive_sentence_intersect(sentence1, sentence2)
    print(result)

    print()


def test_wordlength():
    import wordlength
    print('Sentence intersect')

    word = '  world!  '

    print(f'Word: "{word}"')

    result = wordlength.recursive_word_length(word)
    print(result)

    print()


def test_wordswap():
    import wordswap
    print('Swap first and last words')

    sentence = 'Hello world, world hello, world'

    print(f'Sentence: "{sentence}"')

    result = wordswap.recursive_word_swap(sentence)
    print(result)

    print()


def main():
    test_substr()
    test_wordcount()
    test_wordmatch()
    test_wordfind()
    test_wordreplace()
    test_sentencereverse()
    test_sentenceintersect()
    test_wordlength()
    test_wordswap()


if __name__ == '__main__':
    main()
