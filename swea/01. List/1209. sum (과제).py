T= 10

for test in range(1, T+1):
    test_num = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합을 구한 리스트 만들기 -> max값 구하기
    i_sum_lst = []
    for i in range(100):
        i_sum_lst.append(sum(lst[i]))

    max_i = max(i_sum_lst)


    # 각 열의 합을 구한 리스트 만들기 -> max 값 구하기
    j_sum_lst = []
    for j in range(100):
        j_total = 0
        for i in range(100):
            j_total += lst[i][j]
        j_sum_lst.append(j_total)

    max_j = max(j_sum_lst)

    # 대각선(우하향) 합 구하기
    cross_right = []
    for i in range(100):
        for j in range(100):
            if i == j:
                cross_right.append(lst[i][j])

    max_r = sum(cross_right)

    # 대각선(좌하향) 합 구하기
    cross_left = []
    for i in range(100):
        for j in range(100):
            if i == 100-j:
                cross_left.append(lst[i][j])

    max_l = sum(cross_left)


    # 각 행, 열, 대각선의 합 max 값만 모은 리스트 만들기 -> max 값 출력..^^
    max_lst = []
    max_lst.append(max_i)
    max_lst.append(max_j)
    max_lst.append(max_r)
    max_lst.append(max_l)

    print(f'#{test} {max(max_lst)}')
