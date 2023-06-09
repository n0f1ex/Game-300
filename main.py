from cards import define_cards
from player import Player, Bot
from deck import Deck
from karts import Card, Cover, LustCard, CoverCard
from Queen import Masti
import pygame


def rules(last, card, masti):
    tip = list(card)[1]
    if tip == '6':
        if turn == 'player':
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
        elif turn == 'trus':
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
        elif turn == 'balbes':
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
        elif turn == 'byvalyi':
            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)
            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)

    if tip == '7':
        if turn == 'balbes':
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
        elif turn == 'byvalyi':
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
        elif turn == 'player':
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
        elif turn == 'trus':
            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)

    if list(last)[1] == 'Q':
        if turn == 'player':
            p, c, b, k = Masti(WIDTH, HEIGHT, 'P'), Masti(WIDTH, HEIGHT, 'C'), Masti(WIDTH, HEIGHT, 'B'), Masti(WIDTH,
                                                                                                                HEIGHT,
                                                                                                                'K')
            all_sprites.add(p)
            all_sprites.add(c)
            all_sprites.add(b)
            all_sprites.add(k)
            display()
            running = True
            while running:
                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONUP:
                        if p.rect.collidepoint(pygame.mouse.get_pos()):
                            p.destroy()
                            c.destroy()
                            b.destroy()
                            k.destroy()
                            display()
                            return ['PQ', turn, card]
                        elif c.rect.collidepoint(pygame.mouse.get_pos()):
                            p.destroy()
                            c.destroy()
                            b.destroy()
                            k.destroy()
                            display()
                            return ['CQ', turn, card]
                        elif b.rect.collidepoint(pygame.mouse.get_pos()):
                            p.destroy()
                            c.destroy()
                            b.destroy()
                            k.destroy()
                            display()
                            return ['BQ', turn, card]
                        elif k.rect.collidepoint(pygame.mouse.get_pos()):
                            p.destroy()
                            c.destroy()
                            b.destroy()
                            k.destroy()
                            display()
                            return ['KQ', turn, card]
        else:
            mastes = {}
            if turn == 'trus':
                mastes = trus.masti
            elif turn == 'balbes':
                mastes = balbes.masti
            elif turn == 'byvalyi':
                mastes = byvalyi.masti
            if mastes['C'] >= mastes['P'] and mastes['C'] >= mastes['B'] and mastes['C'] >= mastes['K']:
                return ['CQ', turn, card]
            elif mastes['P'] >= mastes['C'] and mastes['P'] >= mastes['B'] and mastes['P'] >= mastes['K']:
                return ['PQ', turn, card]
            elif mastes['B'] >= masti['P'] and mastes['B'] >= mastes['C'] and mastes['B'] >= mastes['K']:
                return ['BQ', turn, card]
            elif mastes['K'] >= masti['P'] and mastes['K'] >= mastes['B'] and mastes['K'] >= mastes['C']:
                return ['KQ', turn, card]

    if list(last)[1] == 'T':
        return [card, order[(1 + order.index(turn)) % 4], card]

    if list(last)[1] == 'K' and card == 'PK':
        if turn == 'player':
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
            trus.take(deck.take_card(used))
            used.append(trus.cards()[-1])
        elif turn == 'trus':
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
            balbes.take(deck.take_card(used))
            used.append(balbes.cards()[-1])
        elif turn == 'balbes':
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
            byvalyi.take(deck.take_card(used))
            used.append(byvalyi.cards()[-1])
        elif turn == 'byvalyi':
            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)

            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)

            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)

            c = deck.take_card(used)
            player.take(c)
            taken_card = Card()
            taken_card.init(c, len(player_hand), HEIGHT)
            player_hand.append(taken_card)
            all_sprites.add(taken_card)
            used.append(c)
    return [card, turn, card]


def card_play(bot, take=False):
    crd = LustCard(WIDTH, HEIGHT)
    if take:
        crd.init('cover', WIDTH // 36 * 21, HEIGHT // 2 - 71 * crd.resize // 2)
        all_sprites.add(crd)
        x0, y0 = WIDTH // 36 * 21, HEIGHT // 2 - 71 * crd.resize // 2
        x, y = oppos[bot]
    else:
        crd.init(last, oppos[bot][0], oppos[bot][1])
        all_sprites.add(crd)
        x, y = WIDTH // 2 - 49 * crd.resize // 2, HEIGHT // 2 - 71 * crd.resize // 2
        x0, y0 = oppos[bot]
    v = 20
    a = -1
    v_all = (v * 2 + (v - 1) * a) / 2 * v
    len_x, len_y = (x - x0) / v_all, (y - y0) / v_all
    for t in range(v):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                exit()
        crd.rect.x += len_x * (v - t)
        crd.rect.y += len_y * (v - t)
        display()
    crd.kill()


def card_player(card, pos=-1):
    if card == 'cover':
        crd = LustCard(WIDTH, HEIGHT)
        crd.init('cover', WIDTH // 36 * 21, HEIGHT // 2 - 71 * crd.resize // 2)
        all_sprites.add(crd)
        x0, y0 = WIDTH // 36 * 21, HEIGHT // 2 - 71 * crd.resize // 2
        x, y = pos*49*crd.resize, HEIGHT - 71*crd.resize - crd.margin
    else:
        crd = card
        all_sprites.add(crd)
        x, y = WIDTH // 2 - 49 * crd.resize // 2, HEIGHT // 2 - 71 * crd.resize // 2
        x0, y0 = crd.rect.x, crd.rect.y
    v = 20
    a = -1
    v_all = (v * 2 + (v - 1) * a) / 2 * v
    len_x, len_y = (x - x0) / v_all, (y - y0) / v_all
    for t in range(v):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                exit()
        crd.rect.x += len_x * (v - t)
        crd.rect.y += len_y * (v - t)
        display()
    crd.kill()


def display():
    screen.fill(GREEN)

    clock.tick(FPS)

    all_sprites.update()
    all_sprites.draw(screen)

    screen.blit(textplayer, (20, HEIGHT - 200))
    screen.blit(texttrus, (20, 190))
    screen.blit(textbalbes, (WIDTH // 2 - 149, 0))
    screen.blit(textbyvalyi, (425, 190))
    screen.blit(texttruscards, (40, 250))
    screen.blit(textbalbescards, (WIDTH // 2 - 30, 50))
    screen.blit(textbyvalyicards, (620, 250))
    screen.blit(textdeckcards, (WIDTH - 300, HEIGHT // 2 - 71))

    pygame.display.flip()


def round_end():
    run = True

    display()
    if list(last)[1] == 'Q':
        tplayer = font.render('Твои очки: +' + str(player.awerall * (deck.multi + 2)), True, (200, 200, 200))
        ttrus = font.render('Трус: +' + str(trus.awerall * (deck.multi + 2)), True, (200, 200, 200))
        tbalbes = font.render('Балбес: +' + str(balbes.awerall * (deck.multi + 2)), True, (200, 200, 200))
        tbyvalyi = font.render('Бывалый: +' + str(byvalyi.awerall * (deck.multi + 2)), True, (200, 200, 200))
    else:
        tplayer = font.render('Твои очки: +' + str(player.awerall * (deck.multi)), True, (200, 200, 200))
        ttrus = font.render('Трус: +' + str(trus.awerall * (deck.multi)), True, (200, 200, 200))
        tbalbes = font.render('Балбес: +' + str(balbes.awerall * (deck.multi)), True, (200, 200, 200))
        tbyvalyi = font.render('Бывалый: +' + str(byvalyi.awerall * (deck.multi)), True, (200, 200, 200))

    fadeout = pygame.Surface((WIDTH, HEIGHT))
    fadeout = fadeout.convert()
    fadeout.fill((0, 0, 0))

    for f in range(1, 255 // 5):
        eve = pygame.event.get()
        for events in eve:
            if events.type == pygame.MOUSEBUTTONUP:
                return 0
            elif events.type == pygame.QUIT:
                exit()
        display()

        fadeout.blit(tplayer, (20, HEIGHT - 200))
        fadeout.blit(ttrus, (20, 190))
        fadeout.blit(tbalbes, (WIDTH // 2 - 149, 0))
        fadeout.blit(tbyvalyi, (425, 190))
        fadeout.set_alpha(f * 5)
        screen.blit(fadeout, (0, 0))
        pygame.display.flip()


def round_start():
    tplayer = font.render('Твои очки: ' + str(player.awerall * (deck.multi + 2)), True, (200, 200, 200))
    ttrus = font.render('Трус: ' + str(trus.awerall * (deck.multi + 2)), True, (200, 200, 200))
    tbalbes = font.render('Балбес: ' + str(balbes.awerall * (deck.multi + 2)), True, (200, 200, 200))
    tbyvalyi = font.render('Бывалый: ' + str(byvalyi.awerall * (deck.multi + 2)), True, (200, 200, 200))

    fadeout = pygame.Surface((WIDTH, HEIGHT))
    fadeout = fadeout.convert()
    screen.fill((0, 0, 0))

    for f in range(1, 255 // 2):
        fadeout.fill(GREEN)

        clock.tick(FPS)

        all_sprites.update()
        all_sprites.draw(fadeout)

        fadeout.blit(textplayer, (20, HEIGHT - 200))
        fadeout.blit(texttrus, (20, 190))
        fadeout.blit(textbalbes, (WIDTH // 2 - 149, 0))
        fadeout.blit(textbyvalyi, (425, 190))
        fadeout.blit(texttruscards, (40, 250))
        fadeout.blit(textbalbescards, (WIDTH // 2 - 30, 50))
        fadeout.blit(textbyvalyicards, (620, 250))
        fadeout.blit(textdeckcards, (WIDTH - 300, HEIGHT // 2 - 71))

        eve = pygame.event.get()
        for events in eve:
            if events.type == pygame.MOUSEBUTTONUP:
                return 0
            elif events.type == pygame.QUIT:
                exit()
        screen.blit(tplayer, (20, HEIGHT - 200))
        screen.blit(ttrus, (20, 190))
        screen.blit(tbalbes, (WIDTH // 2 - 149, 0))
        screen.blit(tbyvalyi, (425, 190))
        fadeout.set_alpha(f * 3)
        screen.blit(fadeout, (0, 0))
        pygame.display.flip()


WIDTH, HEIGHT = 720, 960  # ширина игрового окна, высота игрового окна
FPS = 20  # частота кадров в секунду

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FadeIn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 300")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('serif', 48)
fontnum = pygame.font.SysFont('serif', 128)
fontLarge = pygame.font.SysFont('serif', 100)

cards = define_cards()
chervy, bubi, krecti, piki = cards[0:9].copy(), cards[9:18].copy(), cards[18:27].copy(), cards[27:36].copy()

player, trus, balbes, byvalyi = Player('player'), Bot('trus'), Bot('balbes'), Bot('byvalyi')

pl1, pl2, pl3 = CoverCard(20, 250), CoverCard(WIDTH // 2 - 49, 50), CoverCard(600, 250)
oppos = [[20, 250], [WIDTH // 2 - 49, 50], [600, 250]]
anim_len = 15
all_sprites.add(pl1)
all_sprites.add(pl2)
all_sprites.add(pl3)

koloda = Cover()
all_sprites.add(koloda)
koloda.init(WIDTH, HEIGHT)
deck = Deck()
turn = 'trus'

order = ['player', 'trus', 'balbes', 'byvalyi']

while player.score() <= 300 and trus.score() <= 300 and balbes.score() <= 300 and byvalyi.score() <= 300:

    deck.reshuffle([], new=True)

    used = []
    last = 'cover'

    textplayer = font.render('Твои очки: ' + str(player.score()), True, (0, 0, 0))
    texttrus = font.render('Трус: ' + str(trus.score()), True, (0, 0, 0))
    textbalbes = font.render('Балбес: ' + str(balbes.score()), True, (0, 0, 0))
    textbyvalyi = font.render('Бывалый: ' + str(byvalyi.score()), True, (0, 0, 0))

    if len(trus.cards()) < 10:
        texttruscards = fontnum.render(str(len(trus.cards())), True, (0, 100, 0))
    else:
        texttruscards = fontLarge.render(str(len(trus.cards())), True, (0, 100, 0))

    if len(balbes.cards()) < 10:
        textbalbescards = fontnum.render(str(len(balbes.cards())), True, (0, 100, 0))
    else:
        textbalbescards = fontLarge.render(str(len(balbes.cards())), True, (0, 100, 0))

    if len(byvalyi.cards()) < 10:
        textbyvalyicards = fontnum.render(str(len(byvalyi.cards())), True, (0, 100, 0))
    else:
        textbyvalyicards = fontLarge.render(str(len(byvalyi.cards())), True, (0, 100, 0))

    if len(deck.left) < 10:
        textdeckcards = fontnum.render(str(len(deck.left)), True, (0, 100, 0))
    else:
        textdeckcards = fontLarge.render(str(len(deck.left)), True, (0, 100, 0))

    player_hand = []
    round_start()

    for i in range(3):
        card_player('cover', len(player_hand))
        c = deck.take_card(used)
        player.take(c)
        taken_card = Card()
        taken_card.init(c, len(player_hand), HEIGHT)
        player_hand.append(taken_card)
        all_sprites.add(taken_card)

        trus.take(deck.take_card(used))
        card_play(0, take=True)
        balbes.take(deck.take_card(used))
        card_play(1, take=True)
        byvalyi.take(deck.take_card(used))
        card_play(2, take=True)

    used.extend(player.cards())
    used.extend(trus.cards())
    used.extend(balbes.cards())
    used.extend(byvalyi.cards())

    if turn == 'player':
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEMOTION:
                for i in player_hand:
                    if i.rect.collidepoint(pygame.mouse.get_pos()):
                        i.on_hover(last, pygame.mouse.get_pos(), start=True)
                    else:
                        i.not_hover(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                exit()
            print(player.cards())
            if event.type == pygame.MOUSEBUTTONUP:
                i = 0
                repos = False
                ind = -1
                while i < len(player_hand):
                    print(player.cards())
                    if player_hand[i].rect.collidepoint(pygame.mouse.get_pos()) and not repos:
                        if i == len(player_hand):
                            for i in player_hand:
                                print(i.card)
                            breakpoint()
                        player.play(i)
                        played_card = player_hand[i].on_click(last, pygame.mouse.get_pos(), start=True)
                        if played_card != -1:
                            ind = i
                            repos = True
                    elif repos:
                        player_hand[i].reposition(i - 1)
                    i += 1
                    if repos:
                        running = False
                        card_player(player_hand[ind])
                        last, turn, use = rules(player.played(played_card), played_card, player.masti)
                        player_hand[ind].played()
                        player_hand.pop(ind)
                        used.append(use)
                        break
        if list(last)[1] == '8':
            running = True
            if len(deck.left) < 10:
                textdeckcards = fontnum.render(str(len(deck.left)), True, (0, 100, 0))
            else:
                textdeckcards = fontLarge.render(str(len(deck.left)), True, (0, 100, 0))
            LastCard.init(last)
            display()

    elif turn == 'trus':
        last = trus.played(0)
        card_play(0)
    elif turn == 'balbes':
        last = balbes.played(0)
        card_play(1)
    elif turn == 'byvalyi':
        last = byvalyi.played(0)
        card_play(2)

    LastCard = LustCard(WIDTH, HEIGHT)
    LastCard.init(last)
    all_sprites.add(LastCard)

    if len(trus.cards()) < 10:
        texttruscards = fontnum.render(str(len(trus.cards())), True, (0, 100, 0))
    else:
        texttruscards = fontLarge.render(str(len(trus.cards())), True, (0, 100, 0))

    if len(balbes.cards()) < 10:
        textbalbescards = fontnum.render(str(len(balbes.cards())), True, (0, 100, 0))
    else:
        textbalbescards = fontLarge.render(str(len(balbes.cards())), True, (0, 100, 0))

    if len(byvalyi.cards()) < 10:
        textbyvalyicards = fontnum.render(str(len(byvalyi.cards())), True, (0, 100, 0))
    else:
        textbyvalyicards = fontLarge.render(str(len(byvalyi.cards())), True, (0, 100, 0))

    if len(deck.left) < 10:
        textdeckcards = fontnum.render(str(len(deck.left)), True, (0, 100, 0))
    else:
        textdeckcards = fontLarge.render(str(len(deck.left)), True, (0, 100, 0))

    while player.out() and trus.out() and balbes.out() and byvalyi.out():
        if deck.shuf:
            deck.shuf = False
            used = [last]
            used.extend(player.cards())
            used.extend(trus.cards())
            used.extend(balbes.cards())
            used.extend(byvalyi.cards())

        turn = order[(1 + order.index(turn)) % 4]

        if turn == 'trus':
            played = False
            while list(last)[1] == '8' or not played:
                played = True
                play = trus.turn(last)
                if play == -1:
                    trus.take(deck.take_card(used))
                    play = trus.turn(last)
                    use = trus.cards()[-1]
                    if play != -1:
                        last, turn, use = rules(trus.played(play), play, trus.masti)
                    used.append(use)
                else:
                    last, turn, use = rules(trus.played(play), play, trus.masti)
                    used.append(use)
                    # /////////////////визуализациятруса//////////////////////
                if play != -1:
                    card_play(0)
                else:
                    card_play(0, take=True)
                if list(last)[1] == '8':
                    played = False
                    display()
                    pygame.time.delay(500)

        elif turn == 'balbes':
            played = False
            while list(last)[1] == '8' or not played:
                played = True
                play = balbes.turn(last)
                if play == -1:
                    balbes.take(deck.take_card(used))
                    play = balbes.turn(last)
                    use = balbes.cards()[-1]
                    if play != -1:
                        last, turn, use = rules(balbes.played(play), play, balbes.masti)
                    used.append(use)
                else:
                    last, turn, use = rules(balbes.played(play), play, balbes.masti)
                    used.append(use)
                    # /////////////////balbes//////////////////////
                if play != -1:
                    card_play(1)
                else:
                    card_play(1, take=True)
                if list(last)[1] == '8':
                    played = False
                    display()
                    pygame.time.delay(500)

        elif turn == 'byvalyi':
            played = False
            while list(last)[1] == '8' or not played:
                play = byvalyi.turn(last)
                played = True
                if play == -1:
                    byvalyi.take(deck.take_card(used))
                    play = byvalyi.turn(last)
                    use = byvalyi.cards()[-1]
                    if play != -1:
                        last, turn, use = rules(byvalyi.played(play), play, byvalyi.masti)
                    used.append(use)
                else:
                    last, turn, use = rules(byvalyi.played(play), play, byvalyi.masti)
                    used.append(use)
                    # /////////////////byvalyi//////////////////////
                if play != -1:
                    card_play(2)
                else:
                    card_play(2, take=True)
                if list(last)[1] == '8':
                    played = False
                    display()
                    pygame.time.delay(500)

        elif turn == 'player':
            running = True
            card_taken = '__'
            while running:
                display()
                p_cards = player.cards()
                for i in player_hand:
                    if i.rect.collidepoint(pygame.mouse.get_pos()):
                        i.on_hover(last, pygame.mouse.get_pos())
                    else:
                        i.not_hover(pygame.mouse.get_pos())
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEMOTION:
                        for i in player_hand:
                            if i.rect.collidepoint(pygame.mouse.get_pos()):
                                i.on_hover(last, pygame.mouse.get_pos())
                            else:
                                i.not_hover(pygame.mouse.get_pos())
                    if event.type == pygame.QUIT:
                        exit()
                    print(player.cards())
                    if event.type == pygame.MOUSEBUTTONUP:
                        if koloda.rect.collidepoint(pygame.mouse.get_pos()):
                            card_player('cover', len(player_hand))
                            c = deck.take_card(used)
                            player.take(c)
                            taken_card = Card()
                            taken_card.init(c, len(player_hand), HEIGHT)
                            player_hand.append(taken_card)
                            all_sprites.add(taken_card)
                            running = False
                            card_taken = c
                            used.append(c)
                            break
                        else:
                            i = 0
                            repos = False
                            ind = -1
                            while i < len(player_hand):
                                print(player.cards())
                                if player_hand[i].rect.collidepoint(pygame.mouse.get_pos()) and not repos:
                                    if i == len(player_hand):
                                        for i in player_hand:
                                            print(i.card)
                                        breakpoint()
                                    player.play(i)
                                    played_card = player_hand[i].on_click(last, pygame.mouse.get_pos())
                                    if played_card != -1:
                                        ind = i
                                        repos = True
                                elif repos:
                                    player_hand[i].reposition(i - 1)
                                i += 1
                            if repos:
                                running = False
                                card_player(player_hand[ind])
                                last, turn, use = rules(player.played(played_card), played_card, player.masti)
                                player_hand[ind].played()
                                player_hand.pop(ind)
                                used.append(use)
                                break
                if list(last)[1] == '8':
                    running = True
                    if len(deck.left) < 10:
                        textdeckcards = fontnum.render(str(len(deck.left)), True, (0, 100, 0))
                    else:
                        textdeckcards = fontLarge.render(str(len(deck.left)), True, (0, 100, 0))
                    LastCard.init(last)
                    display()

        if len(trus.cards()) < 10:
            texttruscards = fontnum.render(str(len(trus.cards())), True, (0, 100, 0))
        else:
            texttruscards = fontLarge.render(str(len(trus.cards())), True, (0, 100, 0))

        if len(balbes.cards()) < 10:
            textbalbescards = fontnum.render(str(len(balbes.cards())), True, (0, 100, 0))
        else:
            textbalbescards = fontLarge.render(str(len(balbes.cards())), True, (0, 100, 0))

        if len(byvalyi.cards()) < 10:
            textbyvalyicards = fontnum.render(str(len(byvalyi.cards())), True, (0, 100, 0))
        else:
            textbyvalyicards = fontLarge.render(str(len(byvalyi.cards())), True, (0, 100, 0))

        if len(deck.left) < 10:
            textdeckcards = fontnum.render(str(len(deck.left)), True, (0, 100, 0))
        else:
            textdeckcards = fontLarge.render(str(len(deck.left)), True, (0, 100, 0))

        LastCard.init(last)
        display()
        pygame.time.delay(500)

    display()

    textplayer = font.render('Твои очки: ' + str(player.score()), True, (0, 0, 0))
    texttrus = font.render('Трус: ' + str(trus.score()), True, (0, 0, 0))
    textbalbes = font.render('Балбес: ' + str(balbes.score()), True, (0, 0, 0))
    textbyvalyi = font.render('Бывалый: ' + str(byvalyi.score()), True, (0, 0, 0))

    if not player.out():
        textplayer = font.render('Твои очки: ' + str(player.score()), True, (0, 255, 0))
    if not trus.out():
        texttrus = font.render('Трус: ' + str(trus.score()), True, (0, 255, 0))
    if not balbes.out():
        textbalbes = font.render('Балбес: ' + str(balbes.score()), True, (0, 255, 0))
    if not byvalyi.out():
        textbyvalyi = font.render('Бывалый: ' + str(byvalyi.score()), True, (0, 255, 0))

    round_end()

    for i in player_hand:
        i.played()
    if list(last)[1] == 'Q':
        player.end(deck.end() + 2)
        trus.end(deck.end() + 2)
        balbes.end(deck.end() + 2)
        byvalyi.end(deck.end() + 2)
    else:
        player.end(deck.end())
        trus.end(deck.end())
        balbes.end(deck.end())
        byvalyi.end(deck.end())

    if player.score() % 100 == 0:
        player.awerall = 0
    elif trus.score() % 100 == 0:
        trus.awerall = 0
    elif balbes.score() % 100 == 0:
        balbes.awerall = 0
    elif byvalyi.score() % 100 == 0:
        byvalyi.awerall = 0

    # Экран окончания раунда

# Конченый экран

textplayer = font.render('Твои очки: ' + str(player.score()), True, (0, 0, 0))
texttrus = font.render('Трус: ' + str(trus.score()), True, (0, 0, 0))
textbalbes = font.render('Балбес: ' + str(balbes.score()), True, (0, 0, 0))
textbyvalyi = font.render('Бывалый: ' + str(byvalyi.score()), True, (0, 0, 0))

if player.score() > 300:
    textplayer = font.render('Твои очки: ' + str(player.score()), True, (255, 0, 0))
if trus.score() > 300:
    texttrus = font.render('Трус: ' + str(trus.score()), True, (255, 0, 0))
if balbes.score() > 300:
    textbalbes = font.render('Балбес: ' + str(balbes.score()), True, (255, 0, 0))
if byvalyi.score() > 300:
    textbyvalyi = font.render('Бывалый: ' + str(byvalyi.score()), True, (255, 0, 0))

display()

screen.fill(BLUE)

all_sprites.update()
all_sprites.draw(screen)

screen.blit(textplayer, (20, HEIGHT - 200))
screen.blit(texttrus, (20, 190))
screen.blit(textbalbes, (WIDTH // 2 - 149, 0))
screen.blit(textbyvalyi, (425, 190))
screen.blit(texttruscards, (40, 250))
screen.blit(textbalbescards, (WIDTH // 2 - 30, 50))
screen.blit(textbyvalyicards, (620, 250))
screen.blit(textdeckcards, (WIDTH - 300, HEIGHT // 2 - 71))

pygame.display.flip()
pygame.time.delay(10000)
