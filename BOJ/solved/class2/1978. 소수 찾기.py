'''
소수가 몇개인지 찾는 프로그램
소수란, 1과 자기 자신 외에는 약수를 가지지 않는 수
그렇다면 소수를 어떻게 판단해야할까.... 걍 노가다해야하나
'''
N = int(input())
nums = map(int, input().split())

decimal = 0
for n in nums:
    for i in range(2, n+1):
        if n % i == 0:
            if n == i:
                decimal += 1
            break
print(decimal)

