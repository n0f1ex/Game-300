import os


def define_cards():
    mast, card = ['C', 'B', 'K', 'P'], ['T', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # карта описывается мастьзначение
    cards = []
    for m in mast:
        for c in card:
            cards.append(os.path.abspath('sprites/' + m + c + '.png'))
    # создание массива карт
    return cards
