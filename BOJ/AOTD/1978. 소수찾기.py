N = int(input())

numbers = map(int, input().split())

cnt = 0
for number in numbers:
    # 소수는 1보다 큰 자연수 중에서
    if number > 1:
        # 1과 자기 외에 다른 수로 나누어떨어지지 않는 수
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            cnt += 1

print(cnt)
