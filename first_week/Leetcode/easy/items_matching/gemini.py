def countMatches(items, ruleKey, ruleValue):
    """
    Counts the number of items matching a rule.

    Args:
        items: A list of lists where each inner list describes an item.
        ruleKey: The key to be matched ("type", "color", or "name").
        ruleValue: The value to be matched.

    Returns:
        The number of items matching the rule.
    """
    count = 0
    for item in items:
        if ruleKey == "type" and item[0] == ruleValue:
            count += 1
        elif ruleKey == "color" and item[1] == ruleValue:
            count += 1
        elif ruleKey == "name" and item[2] == ruleValue:
            count += 1
    return count
