# 내가 제출한 코드
N = int(input())
for i in range(1, N+1):
    star = ['*'] * i
    print(''.join(star))

# 수정한 코드 (위의 코드를 정리함)
N = int(input())
for i in range(1, N+1):
    print('*' * i)
