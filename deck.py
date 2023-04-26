from random import shuffle


class Deck:
    def __init__(self):
        self.left = []
        self.multi = 0
        self.shuf = False

    def reshuffle(self, taken, new=False):
        used = []
        for i in taken:
            used.extend(i)

        if new:
            self.multi = 0

        mast, card = ['C', 'B', 'K', 'P'], ['T', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.left = []
        self.multi += 1

        for m in mast:
            for c in card:
                num = m+c
                if num not in used:
                    self.left.append(num)

        shuffle(self.left)

    def take_card(self, taken):
        if len(self.left) == 0:
            self.reshuffle(taken)
            self.shuf = True
        return self.left.pop()

    def end(self):
        return self.multi
