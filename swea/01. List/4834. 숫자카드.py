t = int(input()) # 테스트 케이스

for i in range(t):
    n = int(input()) # 카드 장수
    cards = list(map(int, input())) # 카드 숫자 리스트
    max_cards = max(cards) # 카드 중 가장 큰 값

    cnt = [0] * (max_cards + 1)
    for j in cards:
        cnt[j] += 1

    cnt.reverse() # 뒤집어진 cnt
    n1 = max(cnt)
    c1 = cnt.index(n1)

    print(f'#{i+1} {(max_cards - c1)} {n1}')
