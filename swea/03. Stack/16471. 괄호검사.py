T = int(input())
for test in range(1, T+1):
    letters = input()

    solo = []
    for i in letters:
        if i == '(' or i == '{':
            solo.append(i)

        if i == ')':
            if solo != [] and solo[-1] == '(':
                solo.pop(-1)
            else:
                solo.append(i)

        if i == '}':
            if solo != [] and solo[-1] == '{':
                solo.pop(-1)
            else:
                solo.append(i)

    if solo == []:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')

        '(' or i == '{'