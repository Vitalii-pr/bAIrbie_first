def min_repeating_character_difference(text):
    char_idx = {}
    min_diff = float('inf')
    result_char = None

    for idx, char in enumerate(text):
        if char in char_idx:
            diff = idx - char_idx[char]
            if diff < min_diff:
                min_diff = diff
                result_char = char  
        char_idx[char] = idx
    return (min_diff, result_char) if result_char else None
