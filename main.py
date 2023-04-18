from cards import define_cards
from player import Player, Bot
from deck import Deck
from interface import Card, Cover, LustCard, CoverCard
import pygame


def display():
    screen.fill(GREEN)

    clock.tick(FPS)

    all_sprites.update()
    all_sprites.draw(screen)

    screen.blit(textplayer, (20, HEIGHT - 200))
    screen.blit(texttrus, (20, 190))
    screen.blit(textbalbes, (WIDTH // 2 - 149, 0))
    screen.blit(textbyvalyi, (425, 190))

    pygame.display.flip()


WIDTH = 720  # ширина игрового окна
HEIGHT = 960  # высота игрового окна
FPS = 20  # частота кадров в секунду

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 300")
global clock
clock = pygame.time.Clock()
global all_sprites
all_sprites = pygame.sprite.Group()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('serif', 48)

cards = define_cards()
chervy, bubi, krecti, piki = cards[0:9].copy(), cards[9:18].copy(), cards[18:27].copy(), cards[27:36].copy()

player, trus, balbes, byvalyi = Player('player'), Bot('trus'), Bot('balbes'), Bot('byvalyi')

pl1, pl2, pl3 = CoverCard(20, 250), CoverCard(WIDTH//2 - 49, 50),  CoverCard(600, 250)
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

    textplayer = font.render('Твои очки: ' + str(player.score()), True, (0, 0, 0))
    texttrus = font.render('Трус: ' + str(trus.score()), True, (0, 0, 0))
    textbalbes = font.render('Балбес: ' + str(balbes.score()), True, (0, 0, 0))
    textbyvalyi = font.render('Бывалый: ' + str(byvalyi.score()), True, (0, 0, 0))

    player_hand = []

    for i in range(3):
        c = deck.take_card()
        player.take(c)
        taken_card = Card()
        taken_card.init(c, len(player_hand), HEIGHT)
        player_hand.append(taken_card)
        all_sprites.add(taken_card)

        trus.take(deck.take_card())
        balbes.take(deck.take_card())
        byvalyi.take(deck.take_card())

    if turn == 'player':
        last = player.played(0)
    elif turn == 'trus':
        last = trus.played(0)
    elif turn == 'balbes':
        last = balbes.played(0)
    elif turn == 'byvalyi':
        last = byvalyi.played(0)

    LastCard = LustCard(WIDTH, HEIGHT)
    LastCard.init(last)
    all_sprites.add(LastCard)

    turn = order[(1 + order.index(turn)) % 4]

    while player.out() and trus.out() and balbes.out() and byvalyi.out():
        turn = order[(1 + order.index(turn)) % 4]

        if turn == 'trus':
            play = trus.turn(last)
            if play == -1:
                trus.take(deck.take_card())
                play = trus.turn(last)
                if play != -1:
                    last = trus.played(play)
                    # /////////////////визуализациятруса//////////////////////
            else:
                last = trus.played(play)
                # /////////////////визуализациятруса//////////////////////

        elif turn == 'balbes':
            play = balbes.turn(last)
            if play == -1:
                balbes.take(deck.take_card())
                play = balbes.turn(last)
                if play != -1:
                    last = balbes.played(play)
                    # /////////////////balbes//////////////////////
            else:
                last = balbes.played(play)
                # /////////////////balbes//////////////////////

        elif turn == 'byvalyi':
            play = byvalyi.turn(last)
            if play == -1:
                byvalyi.take(deck.take_card())
                play = byvalyi.turn(last)
                if play != -1:
                    last = byvalyi.played(play)
                    # /////////////////byvalyi//////////////////////
            else:
                last = byvalyi.played(play)
                # /////////////////byvalyi//////////////////////

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
                    print(event.type)
                    if event.type == pygame.MOUSEBUTTONUP:
                        if koloda.rect.collidepoint(pygame.mouse.get_pos()):
                            c = deck.take_card()
                            player.take(c)
                            taken_card = Card()
                            taken_card.init(c, len(player_hand), HEIGHT)
                            player_hand.append(taken_card)
                            all_sprites.add(taken_card)
                            running = False
                            card_taken = c
                            break
                        else:
                            i = 0
                            repos = False
                            ind = -1
                            while i < len(player_hand):
                                if player_hand[i].rect.collidepoint(pygame.mouse.get_pos()) and not repos:
                                    if i == len(player_hand):
                                        for i in player_hand:
                                            print(i.card)
                                        print(player.cards())
                                        breakpoint()
                                    player.play(i)
                                    played_card = player_hand[i].on_click(last, pygame.mouse.get_pos())
                                    if played_card == -1:
                                        continue
                                    ind = i
                                    repos = True
                                elif repos:
                                    player_hand[i].reposition(i-1)
                                i += 1
                            if repos:
                                running = False
                                last = player.played(ind)
                                player_hand[ind].played()
                                player_hand.pop(ind)
                                break

        LastCard.init(last)
        display()

    for i in player_hand:
        i.played()
    player.end()
    trus.end()
    balbes.end()
    byvalyi.end()
