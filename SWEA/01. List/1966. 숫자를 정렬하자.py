T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N-1):
        j_lst = []
        for j in range(i+1, N):
            j_lst.append(lst[j])
        m = j_lst.index(min(j_lst))

        if lst[i] > lst[m+1+i]:
            lst[i], lst[m + 1 + i] = lst[m+1+i], lst[i]
        else:
            pass

    print(f'#{test}', end=' ')
    for i in lst:
        print(i, end= ' ')
    print()