T = int(input())
for test in range(1, T+1):
    # letters = list(map(str, input()))
    #
    # # 리스트로 변환해서 뒤집고 다시 문자열로 변환해서 비교하기
    # l = len(letters)
    # reversed_lst = []
    # for i in range(l):
    #     reversed_lst.append(letters[l-1-i])
    #
    # reversed_letters = ''.join(str(s) for s in reversed_lst)
    # right_letters = ''.join(str(s) for s in letters)
    #
    # if reversed_letters == right_letters:
    #     print(f'#{test} 1')
    # else:
    #     print(f'#{test} 0')



    letters = input()

    # 문자열의 길이 구하기
    length = 0
    for i in letters:
        length += 1

    cnt = 0
    for j in range(length):
        if letters[j] != letters[length-1-j]:
            cnt += 1

    if cnt > 0:
        print(f'#{test} 0')
    else:
        print(f'#{test} 1')