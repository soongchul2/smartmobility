import streamlit as st
from PIL import Image
import random

image = Image.open('chi.jpg')
st.image(image, caption = " *** Mister Qi's Calico Jack *** ")

def initialize_deck():
    deck = []
    suits = ['♠', '♣', '♥', '♦']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    random.shuffle(deck)
    return deck

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

def play_game():
    if 'deck' not in st.session_state:
        st.session_state.deck = initialize_deck()

    if 'player_hand' not in st.session_state:
        st.session_state.player_hand = [st.session_state.deck.pop(), st.session_state.deck.pop()]

    if 'dealer_hand' not in st.session_state:
        st.session_state.dealer_hand = [st.session_state.deck.pop(), st.session_state.deck.pop()]

    player_hand = st.session_state.player_hand
    dealer_hand = st.session_state.dealer_hand

    st.write("플레이어의 카드:", player_hand)
    st.write("딜러의 첫 번째 카드:", dealer_hand[0])

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score == 21:
        st.success("플레이어가 블랙잭을 이겼습니다!")
        image = Image.open('yeah.jpg')
        st.image(image, caption = 'Yeah~ You won!!!')
        st.balloons()
        return
    elif dealer_score == 21:
        st.error("딜러가 블랙잭을 이겼습니다!")
        return

    if st.button("카드 받기"):
        player_hand.append(st.session_state.deck.pop())
        player_score = calculate_score(player_hand)
        st.write("플레이어의 카드:", player_hand)
        if player_score > 21:
            st.error("플레이어가 21을 초과하여 패배했습니다!")
            st.session_state.player_hand = None
            st.session_state.dealer_hand = None
            st.session_state.deck = None
            return
        elif player_score == 21:
            st.success("플레이어가 21을 달성했습니다!")
            image = Image.open('yeah.jpg')
            st.image(image, caption = ('Yeah~ You won!!!'))
            st.balloons()

    if player_score < 21:
        if st.button("그만하기"):
            while dealer_score < 17:
                dealer_hand.append(st.session_state.deck.pop())
                dealer_score = calculate_score(dealer_hand)

            st.write("딜러의 카드:", dealer_hand)
            st.write("딜러의 점수:", dealer_score)

            if dealer_score > 21:
                st.success("딜러가 21을 초과하여 플레이어가 승리했습니다!")
                image = Image.open('yeah.jpg')
                st.image(image, caption = ('Yeah~ You won!!!'))
                st.balloons()
            elif dealer_score > player_score:
                st.error("딜러가 플레이어를 이겼습니다!")
            elif dealer_score < player_score:
                st.success("플레이어가 딜러를 이겼습니다!")
                image = Image.open('yeah.jpg')
                st.image(image, caption = ('Yeah~ You won!!!'))
                st.balloons()
            else:
                st.warning("무승부입니다!")
            
            st.session_state.player_hand = None
            st.session_state.dealer_hand = None
            st.session_state.deck = None
    

# 메인 앱
def main():
    st.title("간단한 블랙잭 게임")
    play_game()

if __name__ == '__main__':
    main()
