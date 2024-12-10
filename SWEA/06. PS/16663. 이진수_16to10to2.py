for test in range(1, int(input())+1):
    N, nums = input().split()
    num = int(nums, 16) # 16진수 -> 10진수로 변환

    # 2진수로 바꿔주기
    bi_lst = []
    while num:
        bi = num % 2
        bi_lst.append(bi)
        num = num // 2

    while len(bi_lst) % 4:
        bi_lst.append(0)

    ans = ''
    for b in bi_lst[::-1]: # 리스트 슬라이싱 이용하여 출력하기
        ans += str(b)

    print(f'#{test} {ans}')