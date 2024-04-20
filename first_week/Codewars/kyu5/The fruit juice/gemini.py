### Wrote this code with first prompt

class Jar:
    def __init__(self):
        self.contents = {}  # A dictionary to store the amount of each juice type

    def add(self, amount, kind):
        self.contents[kind] = self.contents.get(kind, 0) + amount

    def pour_out(self, amount):
        total_amount = sum(self.contents.values())
        if total_amount == 0:
            return  # Don't pour out anything if the jar is empty
        fraction_to_remove = min(amount / total_amount, 1)  # Don't remove more than what's there
        for kind in self.contents:
            self.contents[kind] -= self.contents[kind] * fraction_to_remove

    def get_total_amount(self):
        return sum(self.contents.values())

    def get_concentration(self, kind):
        total_amount = self.get_total_amount()
        return self.contents.get(kind, 0) / total_amount if total_amount > 0 else 0
