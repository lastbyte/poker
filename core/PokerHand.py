from core.LookupTables import remaining_cards_table, flush_table_map, remaining_cards_table_map, unique_cards_table_map


class PokerHand:
    def __init__(self, cards):
        if len(cards) != 5:
            raise Exception("Invalid number of cards passed for a Poker hand, Poker allows 5 cards for a valid hand")
        self.cards = cards
        self.hand_value_for_flush_straight_and_high_card = self.calculate_hand_value_for_flush_straight_and_high_card()
        self.hand_value_for_other_cards = self.calculate_hand_value_for_other_cards()
        self.hand_rank = self.calculate_hand_rank()

    def calculate_hand_value_for_flush_straight_and_high_card(self):

        cards_value = 0
        for card in self.cards:
            cards_value = cards_value | card.binary_representation
        return cards_value >> 16
        pass

    def calculate_hand_value_for_other_cards(self):
        hand_prime_val = 1
        for card in self.cards:
            hand_prime_val = hand_prime_val * card.prime
        return hand_prime_val

    def calculate_hand_rank(self):
        hand_rank = 999_999_999_999_999
        hand_type = ""

        # check for flush first
        rank_if_flush = self.get_rank_if_flush()
        if rank_if_flush is not None:
            hand_rank = rank_if_flush if rank_if_flush is not None and rank_if_flush < hand_rank else hand_rank

        # check for straight or high card
        rank_if_unique_cards = self.get_rank_if_straight_or_high_card()
        if rank_if_unique_cards is not None:
            hand_rank = rank_if_unique_cards if rank_if_unique_cards < hand_rank else hand_rank

        # check for all the remaining possibilities
        rank_if_other_wise = self.get_rank_if_other_wise()
        if rank_if_other_wise is not None:
            hand_rank = rank_if_other_wise if rank_if_other_wise < hand_rank else hand_rank
            if hand_rank != 999_999_999_999:
                hand_type = \
                    remaining_cards_table[remaining_cards_table['rank'] == hand_rank].get('hand_type')

        # return [hand_rank, hand_type.values[0] if hand_type is not None and len(hand_type.values) > 0 else -1]
        return hand_rank

    def get_rank_if_flush(self):
        is_flush = 0b0000_0000_0000_0000_1111_0000_0000_0000
        for card in self.cards:
            is_flush = is_flush & card.binary_representation

        if is_flush != 0:
            return flush_table_map.get(self.hand_value_for_flush_straight_and_high_card)
        return 999_999_999_999_999

    def get_rank_if_straight_or_high_card(self):
        return unique_cards_table_map.get(self.hand_value_for_flush_straight_and_high_card)

    def get_rank_if_other_wise(self):
        return remaining_cards_table_map.get(self.hand_value_for_other_cards)

    def __str__(self):
        return "Rank : " + str(self.hand_rank) + " [" + " ".join([card.__str__() for card in self.cards]) + "]"
