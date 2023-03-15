T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # input으로 받아온 리스트 버블정렬(오름차순)하기
    for i in range(N):
        i = (N-1) - i
        for j in range(i):
            if lst[j] >= lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    # 정렬된 리스트에서 차례로 큰 수, 작은 수 뽑아서 특별한 배열한 리스트 만들기
    l = len(lst)
    special_lst = []
    if len(lst) % 2: # 홀수개인 경우 -> 중복되는 값을 어떻게 한번만 넣을까?
        for i in range(l // 2 + 1): # 홀수개의 경우 중앙에도 접근해야하기 때문에 범위를 +1 한다.
            special_lst.append(lst[l - 1 - i])
            if lst[i] != lst[l - 1 - i]: # 조건문 추가 -> 큰값과 작은값이 같지 않을 때만 추가
                special_lst.append(lst[i])

    else: # 짝수개의 리스트
        for i in range(l // 2):
            special_lst.append(lst[l - 1 - i])
            special_lst.append(lst[i])

    print(f'#{test}', end=' ')
    for i in special_lst[:10]: # 정렬된 숫자 10개까지만 출력하기
        print(i, end=' ')
    print()