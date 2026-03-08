# Deck of Cards
# This programe shuffles a deck of cards and deals 5 cards using the Deck of Cards API
# Author: Orla Woods
# Code generated with the help of Copilot and claude.ai, Anthropic

import requests

# Step 1: Shuffle a new deck and get the deck id
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
data = response.json()
# Sanity check to make sure the request was successful (copilot suggested code)
# if not data['success']:
    #print("Error shuffling the deck")
    # exit()

deck_id = data['deck_id']
print(f"Deck ID: {deck_id}")
print(f"Shuffled: {data['shuffled']}")
print("-"*20)
      
# Step 2: Draw 5 cards using the deck_id
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
draw_data = response.json()

# Step 3: Print the value and suit of each card
print("Your 5 cards are:")
for i, card in enumerate(draw_data["cards"], start=1):
    value = card["value"]
    suit = card["suit"]
    print(f"  Card {i}: {value} of {suit}")

print("-" * 20)
print(f"Remaining cards in deck: {draw_data['remaining']}")

# Step 4: Check the hand for pairs, triples, straights, or flush
values = [card["value"] for card in draw_data["cards"]]
suits  = [card["suit"]  for card in draw_data["cards"]]

# Order for checking a straight
order = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]

# Count how many times each value appears
value_counts = {v: values.count(v) for v in set(values)}

# Check for flush (all same suit)
is_flush = len(set(suits)) == 1

# Check for straight (5 consecutive values)
indices = sorted([order.index(v) for v in values if v in order])
is_straight = (len(indices) == 5 and indices[-1] - indices[0] == 4 and len(set(indices)) == 5)

print("\n🃏 Hand Check:")
congratulated = False

if is_flush:
    print(f"  🎉 Flush! All five cards are {suits[0]}. Well done!")
    congratulated = True

if is_straight:
    print("  🎉 Straight! Five cards in a row. Impressive!")
    congratulated = True

for value, count in value_counts.items():
    if count == 3:
        print(f"  🎉 Three of a kind! You have three {value}s. Nice hand!")
        congratulated = True
    elif count == 2:
        print(f"  🎉 Pair! You have a pair of {value}s. Not bad!")
        congratulated = True

if not congratulated:
    print("  No special hand this time — better luck next deal!")