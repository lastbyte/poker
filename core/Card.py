from core.Constants import ranks, suits


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.prime = ranks.get(self.rank)["prime_value"]
        self.binary = ranks.get(self.rank)["binary_value"]
        self.suit = suit
        # calculate the binary representation and set it.
        self.binary_representation = self.convert_card_to_binary()

    def convert_card_to_binary(self):
        card_prime_val = bin(self.prime)[2:].zfill(8)
        card_binary_val = bin(self.binary)[2:].zfill(16)
        card_suit_val = bin(suits.get(self.suit)["binary_value"])[2:].zfill(4)
        card_rank_val = bin(suits.get(self.suit)["binary_value"])[2:].zfill(4)

        # xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx
        #
        # read this from right to left
        # fist 16 bits represent the card
        # next 4 bits represent the suit of the card
        # next 4 bits represent the value of the rank
        # last 8 bits represent the prime value associated with the rank
        #

        bin_val = card_binary_val + card_suit_val + card_rank_val + card_prime_val
        return int(bin_val, 2)

    def __str__(self):
        return "({0}, {1})".format(self.rank, self.suit)
