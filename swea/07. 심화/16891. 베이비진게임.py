T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    #1 카운트 정렬할 빈리스트 만들기
    p1 = [0]*10
    p2 = [0]*10

    winner = 0 # default는 무승부
    cnt = 0 # 카드 뽑는 순서
    for card in cards:
        cnt += 1

        if cnt % 2: # 홀수일 때; p1 카드 뽑기
            p1[card] += 1
        else: # 짝수일 때; p2 카드 뽑기
            p2[card] += 1

        if cnt >= 5: # 각 플레이어가 최소 3장 이상 뽑았을 때 부터 baby gin 검사한다.
            # triplet 검사 먼저
            for i in range(10):
                if p1[i] >= 3:
                    winner = 1
                    break
                elif p2[i] >= 3:
                    winner = 2
                    break

            # run 검사
            if winner == 0:
                for j in range(8):
                    if p1[j] and p1[j+1] and p1[j+2] >= 1:
                        winner = 1
                        break
                    elif p2[j] and p2[j+1] and p2[j+2] >= 1:
                        winner = 2
                        break

            if winner != 0: #baby gin 나오면 게임을 종료한다. (break를 어떻게 쓸지 공부하자..!)
                break

    print(f'#{tc} {winner}')