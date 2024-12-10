T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(M):
        lst.append(lst.pop(0))

    print(f'#{test} {lst[0]}')