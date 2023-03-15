t = int(input())

for i in range(t):
    l = list(map(int, input().split()))
    n = l[0] # 정수 개수
    m = l[1] # 구간 개수
    num_lst = list(map(int, input().split()))

    sum_lst = []
    for j in range(n-m+1):
        sum_lst.append(sum(num_lst[j:j+m]))

    print(f'#{i+1} {max(sum_lst) - min(sum_lst)}')
