def most_money(students):
    names = [s.name for s in students]
    money = [s.fives*5 + s.tens*10 + s.twenties*20 for s in students]
    a = all([money[0] == money[i] for i in range(len(money))]) and len(money) != 1
    return 'all' if a else names[money.index(max(money))]
