import sys

def parse_hand(hand: str, bet: int):
    char_count = {}
    best = (None, 0)
    for char in hand:
        if char not in char_count:
            char_count[char] = 1

            if best[1] == 0:
                best = (char, 1)

        else:
            char_count[char] += 1

            if best[1] < char_count[char]:
                best = (char, char_count[char])

    # identify hand category
    if best[1] == 5:
        if best[0] in five_of_kind:
            five_of_kind[best[0]].append((hand,bet))
        else:
            five_of_kind[best[0]] = [(hand,bet)]
    elif best[1] == 4:
        if best[0] in four_of_kind:
            four_of_kind[best[0]].append((hand,bet))
        else:
            four_of_kind[best[0]] = [(hand,bet)]
    elif best[1] == 3 and len(char_count) == 2:
        if best[0] in full_house:
            full_house[best[0]].append((hand,bet))
        else:
            full_house[best[0]] = [(hand,bet)]
    elif best[1] == 3:
        if best[0] in three_of_kind:
            three_of_kind[best[0]].append((hand,bet))
        else:
            three_of_kind[best[0]] = [(hand,bet)]
    elif best[1] == 2 and len(char_count) == 3:
        if best[0] in two_pair:
            two_pair[best[0]].append((hand,bet))
        else:
            two_pair[best[0]] = [(hand,bet)]
    elif best[1] == 2:
        if best[0] in one_pair:
            one_pair[best[0]].append((hand,bet))
        else:
            one_pair[best[0]] = [(hand,bet)]
    else:
        if best[0] in high_card:
            high_card[best[0]].append((hand,bet))
        else:
            high_card[hand[0]] = [(hand,bet)]

def rank_hands(hands: dict, rank: int):
    sum = 0

    while len(hands) > 0:
        best = find_next_best_hand(hands)
        print(f"{rank} x {best} = {rank*best}")
        sum += rank * best
        rank -= 1

    return sum, rank


def card_to_val(card: str):
    if card.isdigit():
        return int(card)
    else:
        match card:
            case "T":
                return 10
            case "J":
                return 11
            case "Q":
                return 12
            case "K":
                return 13
            case "A":
                return 14
                

def find_next_best_hand(hands: dict):
    card_ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for card in card_ranks:
        if card in hands:
            if (len(hands[card]) == 1):
                best_hand = hands[card][0]
                hands[card].remove(best_hand)
                hands.pop(card)
                return int(best_hand[1])
            else:
                best_hand = find_best_of_hands(hands[card])
                tmp_len = len(hands[card])
                hands[card].remove(best_hand)
                return int(best_hand[1])
            
def find_best_of_hands(hands: [(str,str)]):
    curr_best = None
    for hand in hands: 
        if curr_best == None:
            curr_best = hand[0]
            curr_bet = hand[1]
        else:
            res = best_of_two(curr_best, hand[0], curr_bet, hand[1])
            curr_best = res[0]
            curr_bet = res[1]
    return (curr_best, curr_bet)


def best_of_two(curr_hand, new_hand, curr_bet, new_bet):
    for i in range(5):
        if curr_hand[i] != new_hand[i]:
            first_best = card_to_val(curr_hand[i])
            second_best = card_to_val(new_hand[i]) 
            if (first_best > second_best):
                return (curr_hand,curr_bet)
            else:
                return (new_hand,new_bet)

if __name__ == "__main__":
    sys.path.append("../")
    import helper as h

    input = '../inputs/7-test.txt'
    lines = h.read_file(input)

    cards = []
    bets = []

    for line in lines:
        cards_and_bet = line.split(" ")
        cards.append(cards_and_bet[0])
        bets.append(cards_and_bet[1])
    
    five_of_kind = {}
    four_of_kind = {}
    full_house = {}
    three_of_kind = {}
    two_pair = {}
    one_pair = {}
    high_card = {}

    categories = [five_of_kind,
                  four_of_kind,
                  full_house,
                  three_of_kind,
                  two_pair,
                  one_pair,
                  high_card]
    
    for i in range(len(cards)):
        parse_hand(cards[i], bets[i])

    start_rank = len(cards)
    sum = 0
    counter = 0
    for c in categories:
        counter += 1
        print(f"========{counter}/7========")
        part_sum, start_rank = rank_hands(c,start_rank)
        print(f"{sum} + {part_sum} = {sum+part_sum}")
        sum += part_sum
    
    print(sum)
