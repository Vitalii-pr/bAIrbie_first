def min_repeating_character_difference(text):
    res = []
    for ind, el in enumerate(text):
        if el in text[ind + 1:]:
            res.append((text[ind + 1:].find(el) + 1, el))
    return min(res, key = lambda x: x[0]) if len(res) != 0 else None
