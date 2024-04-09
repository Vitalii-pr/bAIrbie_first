class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        crew_weight = self.crew * 1.5
        potential_booty_weight = self.draft - crew_weight
        return potential_booty_weight > 20
