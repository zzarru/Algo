T = int(input())
for test in range(1, T+1):
    str1 = input()
    str2 = input()

    len_1= 0
    for i in str1:
        len_1 += 1

    len_2 = 0
    for i in str2:
        len_2 += 1

    result = 0
    for i in range(len_2+1-len_1):
        if str2[i:i+len_1] == str1:
            result += 1

    print(f'#{test} {result}')

