class Jar:
    '''Jar class to add juices'''

    def __init__(self):
        self.juices = {}
        self.amount = 0

    def add(self, amount, kind):
        '''Enter amount and kind of juice to add this juice to jar'''
        self.juices[kind] = self.juices.get(kind, 0 ) + amount
        self.amount += amount

    def pour_out(self, amount):
        '''Enter amount to pour out from jar'''
        am = amount/self.amount
        if self.amount == 0:
            return 
        self.amount -= amount if amount <= self.amount else 0
        for i in self.juices:
            self.juices[i] -= self.juices[i] * am


    def get_total_amount(self):
        '''Returns amount of all juices in jar'''
        return self.amount

    def get_concentration(self, kind):
        '''Returns concentation of juice in jar'''
        return self.juices.get(kind, 0)/self.amount if self.amount != 0 else 0

        