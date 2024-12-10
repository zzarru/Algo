T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list([0]*N for _ in range(N))

    direct = 1
    cnt = 1
    i = 0
    j = -1

    while N > 0:
        for _ in range(N):
            j = j + direct
            arr[i][j] = cnt
            cnt += 1
        N -= 1
        for _ in range(N):
            i = i + direct
            arr[i][j] = cnt
            cnt += 1
        direct *= -1


    # print(arr)

    print(f'#{test}')
    for i in arr:
        for j in i:
            print(j, end=' ') # 공백을 두고 j의 값이 붙어서 출력된다.
        print() # 전체 for문 한번 돌면 줄 바꾸고 출력