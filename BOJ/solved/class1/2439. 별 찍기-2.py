# # 내 코드
N = int(input())
stars = [' ']*N

for i in range(1, N+1):
    stars[-i] = '*'

    print(''.join(stars))

# #2 이렇게 풀면 더 좋았을까?
N=int(input())
for i in range(1,N+1):
    print(" "*(N-i)+"*"*i) # 문자열 합치기를 사용함
#
# #3 정렬 method 사용하기
N=int(input())

for i in range(1, N+1):
    stars = '*' * i
    print(stars.rjust(N))

'''
.rjust(N) : 전체 N 중 오른쪽 정렬
.center(N): 중앙 정렬
.ljust(N) : 왼쪽 정렬
'''
