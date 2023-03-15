T = int(input())
for test in range(1, T+1):
    N = int(input())

    stack = [[0]*N for _ in range(N)]
    stack[0][0] = 1
    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                stack[i][j] = 1
            else:
                stack[i][j] = stack[i-1][j-1] + stack[i-1][j]

    # 프린트할 때 0을 제외하고 출력하기
    print(f'#{test}')
    for i in stack:
        for j in i:
            if j != 0:
                print(j, end=' ')
        print()