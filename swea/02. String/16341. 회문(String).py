T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    letters = [list(map(str, input())) for _ in range(N)]

    # 가로, 세로 문자열 입력하기; 문자열 더하기 되니까!
    horizon_letters = []
    vertical_letters = []
    for i in range(N):
        horizon_l = ''
        vertical_l = ''
        for j in range(N):
            horizon_l = horizon_l + letters[i][j]
            vertical_l = vertical_l + letters[j][i]

        horizon_letters.append(horizon_l)
        vertical_letters.append(vertical_l)

    # 문자열에서 가능한 M길이 문자 다 뽑기!
    horizon_lst = []
    for i in horizon_letters:
        for j in range(N-M+1):
            horizon_lst.append(i[j:j+M])

    vertical_lst = []
    for i in vertical_letters:
        for j in range(N-M+1):
            vertical_lst.append(i[j:j+M])

    # 뽑아낸 M자 문자 회문 검사하기
    for l in horizon_lst:
        if l == l[::-1]:
            print(f'#{test} {l}')

    for l in vertical_lst:
        if l == l[::-1]:
            print(f'#{test} {l}')
