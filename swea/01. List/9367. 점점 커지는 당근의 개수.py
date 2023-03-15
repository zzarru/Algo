T = int(input())
for test in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    cnt = 1
    cnt_lst =[]
    for i in range(N-1):
        if carrots[i+1] > carrots[i]:
            cnt = cnt + 1
        else: # 굳이 if문을 두개 안써도 됨!
            cnt = 1

        cnt_lst.append(cnt)

    print(f'#{test} {max(cnt_lst)}')