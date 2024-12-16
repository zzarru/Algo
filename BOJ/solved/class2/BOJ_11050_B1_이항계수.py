# 1. 팩토리얼 함수 만들기
def factorial(i):
    ans = 1
    while i != 0:
        ans *= i
        i -= 1
    return ans


# 2. 이항계수
N, K = map(int, input().split())
print(factorial(N) // (factorial(K)*factorial(N-K)))
