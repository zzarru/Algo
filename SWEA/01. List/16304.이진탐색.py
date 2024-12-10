T = int(input())
for test in range(1, T+1):
    page, Pa, Pb = map(int, input().split())

    def searchPage(page, mark):
        start = 1
        end = page
        cnt = 1

        while start < end:
            middle = (start + end) // 2
            if middle == mark:
                break

            elif middle < mark:
                start = middle
                cnt += 1

            else:
                end = middle
                cnt += 1

        return cnt

    player1 = searchPage(page, Pa)
    player2 = searchPage(page, Pb)

    if player1 < player2:
        print(f'#{test} A')
    elif player1 > player2:
        print(f'#{test} B')
    else:
        print(f'#{test} 0')