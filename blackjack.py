import streamlit as st

import random


# 카드 덱 초기화
def initialize_deck():
    deck = []
    suits = ['♠', '♣', '♥', '♦']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    random.shuffle(deck)
    return deck

# 카드 값 계산
def calculate_score(cards):
    score = 0
    num_aces = 0
    for card in cards:
        rank = card[:-1]
        if rank.isnumeric():
            score += int(rank)
        elif rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            num_aces += 1
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

# 게임 실행
def play_game():
    deck = initialize_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    st.write("플레이어의 카드:", player_hand)
    st.write("딜러의 첫 번째 카드:", dealer_hand[0])

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score == 21:
        st.write("플레이어가 블랙잭을 이겼습니다!")
        return
    elif dealer_score == 21:
        st.write("딜러가 블랙잭을 이겼습니다!")
        return

    if st.button("카드 받기"):
        player_hand.append(deck.pop())
        player_score = calculate_score(player_hand)
        st.write("플레이어의 카드:", player_hand)
        if player_score > 21:
            st.write("플레이어가 21을 초과하여 패배했습니다!")
            return
        elif player_score == 21:
            st.write("플레이어가 21을 달성했습니다!")

    if player_score < 21:
        if st.button("그만하기"):
            while dealer_score < 17:
                dealer_hand.append(deck.pop())
                dealer_score = calculate_score(dealer_hand)

            st.write("딜러의 카드:", dealer_hand)
            if dealer_score > 21:
                st.write("딜러가 21을 초과하여 플레이어가 이겼습니다!")
            elif dealer_score > player_score:
                st.write("딜러가 플레이어를 이겼습니다!")
            elif dealer_score < player_score:
                st.write("플레이어가 딜러를 이겼습니다!")
            else:
                st.write("무승부입니다!")

# 메인 앱
def main():
    st.title("간단한 블랙잭 게임")
    play_game()

if __name__ == '__main__':
    main()
