from random import choice


class Game:
    def __init__(self):
        self.deck = {'spade_a': 14, 'spade_2': 2, 'spade_3': 3, 'spade_4': 4,
                     'spade_5': 5, 'spade_6': 6, 'spade_7': 7, 'spade_8': 8, 'spade_9': 9,
                     'spade_10': 10, 'spade_j': 11, 'spade_q': 12, 'spade_k': 13, 'club_a': 14,
                     'club_2': 2, 'club_3': 3, 'club_4': 4, 'club_5': 5, 'club_6': 6, 'club_7': 7, 'club_8': 8,
                     'club_9': 9, 'club_10': 10, 'club_j': 11, 'club_q': 12, 'club_k': 13, 'heart_a': 14,
                     'heart_2': 2, 'heart_3': 3, 'heart_4': 4, 'heart_5': 5, 'heart_6': 6, 'heart_7': 7, 'heart_8': 8,
                     'heart_9': 9, 'heart_10': 10, 'heart_j': 11, 'heart_q': 12, 'heart_k': 13, 'diamond_a': 14,
                     'diamond_2': 2, 'diamond_3': 3, 'diamond_4': 4, 'diamond_5': 5, 'diamond_6': 6,
                     'diamond_7': 7, 'diamond_8': 8, 'diamond_9': 9, 'diamond_10': 10, 'diamond_j': 11, 'diamond_q': 12,
                     'diamond_k': 13}
        self.p1 = {}
        self.p2 = {}
        self.turns = 0
        self.p1_picked = 0
        self.p2_picked = 0
        self.continue_game = True
        self.war_cards = {}

    def separate_deck(self):
        while len(self.deck) != 26:
            chosen_key = choice(list(self.deck))
            self.p1[chosen_key] = self.deck[chosen_key]
            del self.deck[chosen_key]
        self.p2 = self.deck
        game.play_game()

    def play_game(self):
        sim_or_no = input("Would you like to sim to the end?(Yes/No): ")
        if sim_or_no == "Yes":
            game.simulate_game()
        else:
            answer = 'Yes'
            while self.continue_game:
                while answer == 'Yes':
                    p1_card = choice(list(self.p1))
                    p2_card = choice(list(self.p2))
                    if self.p1[p1_card] > self.p2[p2_card]:
                        print("Player 1's Card:", self.p1[p1_card], "\nPlayer 2's Card:", self.p2[p2_card])
                        print('Player 1 Wins!')
                        self.p1[p2_card] = self.p2[p2_card]
                        del self.p2[p2_card]
                    elif self.p1[p1_card] < self.p2[p2_card]:
                        print("Player 1's Card:", self.p1[p1_card], "\nPlayer 2's Card:", self.p2[p2_card])
                        print('Player 2 Wins!')
                        self.p2[p1_card] = self.p1[p1_card]
                        del self.p1[p1_card]
                    elif self.p1[p1_card] == self.p2[p2_card]:
                        print("Player 1's Card:", self.p1[p1_card], "\nPlayer 2's Card:", self.p2[p2_card])
                        print("War")
                        game.card_war()
                        if self.continue_game:
                            if self.p1[self.p1_picked] > self.p2[self.p2_picked]:
                                print("Player 1 Card:", self.p1[self.p1_picked], "\nPlayer 2 Card:",
                                      self.p2[self.p2_picked])
                                print("Player 1 Wins!")
                            if self.p1[self.p1_picked] < self.p2[self.p2_picked]:
                                print("Player 1 Card:", self.p1[self.p1_picked], "\nPlayer 2 Card:",
                                      self.p2[self.p2_picked])
                                print("Player 2 Wins!")
                    print("Player 1 has", len(self.p1), 'cards.')
                    print("Player 2 has", len(self.p2), 'cards.')
                    self.turns += 1
                    if len(self.p1) == 0:
                        print('Player 2 Won The Game!')
                        self.continue_game = False
                        answer = "No"
                        game.end_game()
                    elif len(self.p2) == 0:
                        print('Player 1 Won The Game!')
                        self.continue_game = False
                        answer = "No"
                        game.end_game()
                    else:
                        answer = input('Play next hand?(Yes/No): ')
                        if answer == 'No':
                            self.continue_game = False
                            game.end_game()

    def card_war(self):
        if len(self.p1) < 4:
            print('Player 2 Wins, Player 1 does not have enough cards')
            for z in self.war_cards:
                self.p2[z] = self.war_cards[z]
            self.continue_game = False
            game.end_game()
        elif len(self.p2) < 4:
            print('Player 1 Wins, Player 2 does not have enough cards')
            for i in self.war_cards:
                self.p1[i] = self.war_cards[i]
            self.continue_game = False
            game.end_game()
        if self.continue_game:
            for x in range(0, 3):
                card = choice(list(self.p1))
                self.war_cards[card] = self.p1[card]
                del self.p1[card]
                card2 = choice(list(self.p2))
                self.war_cards[card2] = self.p2[card2]
                del self.p2[card2]
            self.p1_picked = choice(list(self.p1))
            self.p2_picked = choice(list(self.p2))
            if self.p1[self.p1_picked] > self.p2[self.p2_picked]:
                for x in self.war_cards:
                    self.p1[x] = self.war_cards[x]
                self.war_cards.clear()
            elif self.p1[self.p1_picked] < self.p2[self.p2_picked]:
                for y in self.war_cards:
                    self.p2[y] = self.war_cards[y]
                self.war_cards.clear()
            else:
                game.card_war()

    def simulate_game(self):
        print("The game will be simulated")
        while self.continue_game:
            if len(self.p1) == 0:
                self.continue_game = False
                game.end_game()
            elif len(self.p2) == 0:
                self.continue_game = False
                game.end_game()
            else:
                p1_card = choice(list(self.p1))
                p2_card = choice(list(self.p2))
                if self.p1[p1_card] > self.p2[p2_card]:
                    self.p1[p2_card] = self.p2[p2_card]
                    del self.p2[p2_card]
                elif self.p1[p1_card] < self.p2[p2_card]:
                    self.p2[p1_card] = self.p1[p1_card]
                    del self.p1[p1_card]
                elif self.p1[p1_card] == self.p2[p2_card]:
                    game.card_war()
                self.turns += 1

    def end_game(self):
        if not self.continue_game:
            print('The game has ended!')
            print('The game ran for', self.turns, 'turns.')
            print('Player 1 finished with', len(self.p1), 'cards.', '\nPlayer 2 finished with',
                  len(self.p2), 'cards.')


game = Game()
game.separate_deck()
