import itertools

from core.LookupTables import poker_lookup_table
from core.PokerHand import PokerHand


def find_winning_hand(community_cards, player_hands):
    winning_hand = None
    winning_player = -1
    for i, player_hand in enumerate(player_hands):
        total_cards = community_cards + player_hand
        player_best_hand = find_player_best_hand(total_cards)
        if winning_hand is None:
            winning_hand = player_best_hand
            winning_player = "Player " + str(i + 1)
        elif player_best_hand.hand_rank < winning_hand.hand_rank:
            winning_hand = player_best_hand
            winning_player = "Player " + str(i + 1)
    winning_hand_expanded = poker_lookup_table[poker_lookup_table['rank'] == winning_hand.hand_rank]
    return {"winning_hand_rank": winning_hand_expanded['rank'].values[0],
            "winning_hand_type": winning_hand_expanded['hand_type'].values[0],
            "winning_hand": winning_hand_expanded['hand_representation'].values[0],
            "winning_hand_description": winning_hand_expanded['hand_description'].values[0],
            "winning_player": winning_player}


def find_player_best_hand(all_cards):
    winning_hand = None
    all_hands = list(itertools.combinations(all_cards, 5))
    for hand in all_hands:
        poker_hand = PokerHand(hand)
        if winning_hand is None:
            winning_hand = poker_hand
        elif poker_hand.hand_rank < winning_hand.hand_rank:
            winning_hand = poker_hand
    return winning_hand
