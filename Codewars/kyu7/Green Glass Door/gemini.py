def step_through_with(s):
    for i in range(len(s) - 1):
        if s[i].lower() == s[i + 1].lower():
            return True
    return False
