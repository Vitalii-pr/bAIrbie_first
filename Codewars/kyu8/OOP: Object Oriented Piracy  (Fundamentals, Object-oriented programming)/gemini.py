class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        crew_weight = self.crew * 1.5
        draft_without_crew = self.draft - crew_weight
        return draft_without_crew > 20
