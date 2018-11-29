import re


regex = re.compile(r'\w')


def recursive_word_swap(sentence: str, first_word_idx=0, last_word_idx=0):
    last_word_start = sentence.rfind(' ') + 1
    first_word_pos, last_word_pos = first_word_idx, last_word_start + last_word_idx
    fw_char= sentence[first_word_pos]
    lw_char = sentence[last_word_pos] if last_word_pos < len(sentence) else ''

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
