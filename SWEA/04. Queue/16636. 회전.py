T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    # M번 반복했을 때, 인덱스 구하기
    idx = M % N
    print(f'#{test} {queue[idx]}')