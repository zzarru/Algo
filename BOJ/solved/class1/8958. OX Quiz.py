#1 내가 제출한 코드
for _ in range(int(input())):
    total = 0
    score = 0
    for Q in input():
        if Q == 'O':
            score += 1
            total += score
        else:
            score = 0

    print(total)