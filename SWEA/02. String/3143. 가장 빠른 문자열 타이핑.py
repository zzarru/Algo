T = int(input())
for test in range(1, T+1):
    A,B = map(str, input().split())

    match_lst = []
    for i in range(len(A)-len(B)+1):
        match_lst.append(A[i:i+len(B)])

    print(match_lst)

    cnt = 0
    for j in match_lst:
        if j == B:
            cnt += 1

    result = len(A) - (len(B) * cnt) + cnt
    print(f'#{test} {result}')