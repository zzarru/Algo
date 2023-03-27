'''
1) count 배열 만들기 : P1, P2
'''

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    P1 = [0]*10
    P2 = [0]*10

    #2 일단 카드 4장을 뽑는다.
    for i in range(0, 4):
        card = cards[i]
        if i % 2 ==0:
            P1[card] += 1
        else:
            P2[card] += 1
    winner = 0
    #3 카드를 차례로 뽑으면서 run과 triplet 검사하기
    for i in range(4, 12):
            card = cards[i]
            if i % 2 ==0:
                P1[card] += 1
                # run 검사하기
            for j in range(10):
                if P1[j] >= 3:
                    winner = 1
                    break
            for j in range(0, 8):
                if P1[j] == P1[j+1] == P1[j+2]:
                    winner = 1
                    break

        else:
            P2[card] += 1
        for j in range(10):
                if P2[j] >= 3:
                    winner = 2
                    break
            for j in range(0, 8):
                if P2[j] == P1[j+1] == P1[j+2]:
                    winner = 2
                    break

    print(winner)


