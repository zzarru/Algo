def dfs(n):
    global ans
    if n == change:
        ans = max(ans, int("".join(map(str, lst))))
        return

    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            cst = int("".join(map(str, lst)))
            if dct_v.get((n, cst), 0) == 0:
                dfs(n + 1)
                dct_v[(n, cst)] = 1

            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for test in range(1, T + 1):
    numbers, change = input().split()
    change = int(change)
    lst = []
    for number in numbers:
        lst.append(int(number))

    v = []
    dct_v = {}
    L = len(lst)
    ans = 0
    dfs(0)

    print(f'#{test} {ans}')