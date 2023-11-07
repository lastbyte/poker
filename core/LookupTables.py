import pandas as pd
import os
##
poker_lookup_table = pd.read_csv(os.getcwd()+'/poker_lookup_table.csv')
flush_table = \
    pd.DataFrame.copy(poker_lookup_table[(poker_lookup_table['hand_type'] == 'SF') | (poker_lookup_table['hand_type'] == 'F')])

##
unique_cards_table = pd.DataFrame.copy(poker_lookup_table[
    (poker_lookup_table['hand_type'] == 'S') | (
            poker_lookup_table['hand_type'] == 'HC')])

##
remaining_cards_table = pd.DataFrame.copy(poker_lookup_table[
    (poker_lookup_table['hand_type'] != 'SF') & (
            poker_lookup_table['hand_type'] != 'F') & (
            poker_lookup_table['hand_type'] != 'S') & (
            poker_lookup_table['hand_type'] != 'HC')])


flush_table_map = dict(zip(flush_table["hand_value"], flush_table["rank"]))
unique_cards_table_map = dict(zip(unique_cards_table["hand_value"], unique_cards_table["rank"]))
remaining_cards_table_map = dict(zip(remaining_cards_table["hand_prime_value"], remaining_cards_table["rank"]))