# # 테스트 케이스
# t = int(input())
#
# # 테스트 케이스 반복
# for test in range(1, t+1):
#     # k=이동거리, n= 마지막 정류장 번호 m= 충전기가 설치된 정류장의 수
#     k, n, m = list(map(int, input().split()))
#     # 충전기가 설치된 정류장의 번호
#     station = list(map(int, input().split()))
#
#     # 현재 위치 = location, 충전횟수 = charge
#     location = 0
#     charge = 0
#     while location + k < n:
#         for move in range(k, 0, -1):
#             if (location + move) in station:
#                 location += move
#                 charge += 1
#                 break
#
# print(f'#{test} {charge}')

T = int(input())

for test in range(1, T+1):
    K, N, M = list(map(int, input().split()))

    station = list(map(int, input().split()))
    charge = location = 0

    while location + K < N:
        for i in range(K, 0, -1):
            if (location + i) in station:
                location += i
                charge += 1
                break
        else:
            charge = 0
            break

    print(f'#{test} {charge}')
