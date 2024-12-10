T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # 인덱스랑 피자(치즈양) 같이 리스트로 만들기
    pizzas = list(enumerate(lst))

    # 화덕 크기만큼 피자 넣어주기
    oven = []
    for i in range(N):
        oven.append(pizzas.pop(0))

    # 화덕에서 피자 꺼내서 치즈 확인하기
    while oven: # 피자가 남아있을 때까지
        idx, cheese = oven.pop(0)
        cheese = cheese // 2

        if cheese != 0: # 치즈가 남아있는 경우
            oven.append((idx, cheese))
        else: # 피자완성 -> 꺼내고
            if pizzas: # 남아있는 피자 있으면 화덕에 넣어줘라
                oven.append(pizzas.pop(0))
            elif not oven:
                print(f'#{test} {idx+1}')