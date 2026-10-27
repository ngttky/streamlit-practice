import random


def draw_cards():
    suits = ("spades", "hearts", "diamonds", "clubs")
    deck = [
        {"suit": suit, "rank": rank}
        for suit in suits
        for rank in range(1, 14)
    ]
    return random.sample(deck, 2)

def judge(base_rank, result_rank, choice):
    # 同じ数字なら引き分け
    if base_rank == result_rank:
        return "draw"

    # Highを選んだ場合
    if choice == "High":
        if result_rank > base_rank:
            return "win"
        else:
            return "lose"

    # Lowを選んだ場合
    if choice == "Low":
        if result_rank < base_rank:
            return "win"
        else:
            return "lose"

    return "invalid"