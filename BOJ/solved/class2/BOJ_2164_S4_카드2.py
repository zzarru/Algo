from collections import deque

N = int(input())
deck = deque()
for card in range(1, N+1):
    deck.append(card)

for _ in range(N-1):
    deck.popleft()
    deck.append(deck.popleft())

print(*deck)

"""
처음엔 그냥 list 를 만들어 pop을 사용했더니 시간초과가 떴다. 
"""