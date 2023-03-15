# 재귀호출을 이용한 거듭제곱 프로그램 만들기
def power(N, M):
    if M == 0: # N**0은 항상 1이므로
        return 1
    else:
        return N * power(N, M-1) # N**M == N * (N**(M-1))

T = 10
for _ in range(1, T + 1):
    test = int(input())
    N, M = map(int, input().split())

    print(f'#{test} {power(N,M)}')