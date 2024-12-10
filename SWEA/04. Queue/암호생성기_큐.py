T = 10
for _ in range(T):
    test = int(input())
    lst = list(map(int, input().split()))

    while lst[-1] != 0:
        for i in range(1, 6):
            v = lst.pop(0)
            v = v - i
            if v > 0:
                lst.append(v)
            else:
                lst.append(0)
                break

    print(f'#{test}',*lst)