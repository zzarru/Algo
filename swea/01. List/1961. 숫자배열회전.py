T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전
    arr_90 = []
    for i in range(N):
        lst_90 = []
        for j in range(N):
            lst_90.append(arr[N-1-j][i])
        arr_90.append(lst_90)

    # 180도 회전
    arr_180 = []
    for i in range(N):
        lst_180 = []
        for j in range(N):
            lst_180.append(arr[N-1-i][N-1-j])
        arr_180.append(lst_180)

    # 270도 회전
    arr_270 = []
    for i in range(N):
        lst_270 = []
        for j in range(N):
            lst_270.append(arr[j][N-1-i])
        arr_270.append(lst_270)

    print(f'#{test}')

    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')
        print()

