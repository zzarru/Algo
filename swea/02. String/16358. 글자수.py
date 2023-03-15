T = int(input())
for test in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    cnt_lst = []
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1

        cnt_lst.append(cnt)

    print(f'#{test} {max(cnt_lst)}')