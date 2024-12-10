from collections import deque

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # 피자와 인덱스 같이 받아주기
    pizzas = deque(list(enumerate(lst)))
    oven = deque([])
    # 화덕의 크기만큼 피자 넣어주기
    for _ in range(N):
        oven.append(pizzas.popleft())

    # 오븐에 피자가 들어있는 동안은 계속 반복한다.
    while oven:
        num, cheese = oven.popleft()
        cheese = cheese // 2
        if cheese != 0:
            oven.append((num, cheese))
        else:
            if pizzas:
                oven.append(pizzas.popleft())
            else:
                ans = num + 1

    print(f'#{test} {ans}')

