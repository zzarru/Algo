#1 입력을 list로 받기
numbers = list(map(int, input().split()))

#2 각 자리수의 제곱의 합 구하기
cnt = 0
for number in numbers:
    cnt += number**2

#3 검증수 == 제곱의 합을 10으로 나눈 나머지
ans = cnt % 10
print(ans)