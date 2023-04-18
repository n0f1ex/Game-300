class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.masti = {'C': 0, 'B': 0, 'K': 0, 'P': 0}
        self.value = 0
        self.awerall = 0
        self.cost = {'T': 11, '6': 0, '7': 0, '8': 0, '9': 0, '1': 10, 'J': 10, 'Q': 30, 'K': 10}

    def take(self, card):
        self.hand.append(card)
        self.masti[list(card)[0]] += 1
        if card == 'PK':
            self.value += 30

        self.value += self.cost[list(card)[1]]

    def play(self, num):
        if type(num) != type(0):
            num = self.hand.index(num)
        return self.hand[num]

    def played(self, num):
        if type(num) != type(0):
            num = self.hand.index(num)
        self.masti[list(self.hand[num])[0]] -= 1
        if self.hand[num] == 'PK':
            self.value -= 30
        self.value -= self.cost[list(self.hand[num])[1]]
        return self.hand.pop(num)

    def end(self):
        self.awerall += self.value
        self.value = 0
        self.hand = []
        return self.awerall

    def cards(self):
        return self.hand

    def out(self):
        return len(self.hand) > 0

    def points(self):
        return self.value

    def score(self):
        return self.awerall


class Bot(Player):
    def turn(self, hover):
        priority = ['8', 'T', 'K', 'J', '1', '6', '7', '9', 'Q']
        m, c = list(hover)[0], list(hover)[1]
        available = [[], [], [], [], [], [], [], [], []]
        has_card = False
        for i in self.hand:
            if list(i)[0] == m or list(i)[1] == c:
                available[priority.index(list(i)[1])].append(i)
                has_card = True
        if has_card:
            ind = 0
            while len(available[ind]) == 0:
                ind += 1
            return available[ind][0]
        else:
            return -1
