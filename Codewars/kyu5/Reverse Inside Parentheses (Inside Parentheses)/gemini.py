def reverse_in_parentheses(text):
    """Reverses substrings within parentheses, handling nested cases and parenthesis orientation."""

    if not text or "(" not in text:
        return text

    stack = []
    for i, char in enumerate(text):
        if char == "(":
            stack.append(i)
        elif char == ")":
            start = stack.pop()
            reversed_part = text[start + 1:i].translate(str.maketrans("()", ")("))[::-1]
            text = text[:start] + "(" + reversed_part + ")" + text[i + 1:]

    return text
