def toB():
    global hexa
    ans = ''
    while hexa:
        bi = hexa % 2
        ans += str(bi)
        hexa = hexa // 2

    while len(ans) <4:
        ans += '0'

    rlt = ''
    for a in ans[::-1]:
        rlt += a

    return rlt

T = int(input())
for test in range(1, T+1):
    N, hexas = input().split()
    hex_dic = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    answer = ''
    for hexa in hexas:
        if hexa.isalpha():
            hexa = hex_dic[hexa]

        else:
            hexa = int(hexa)

        answer += toB()

    print(f'#{test} {answer}')