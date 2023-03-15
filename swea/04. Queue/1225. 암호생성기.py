def circle(pw):
    for i in range(1, 6):
        if pw[0] > i:
            front = pw[0]
            front -= i
            pw.append(front)
            pw.pop(0)

        else:
            front = 0
            pw.append(front)
            pw.pop(0)
            break

    return pw


for _ in range(10):
    test = int(input())
    pw = list(map(int, input().split()))

    while pw[-1] != 0:
        pw = circle(pw)

    print(f'#{test}', end=' ')
    for i in pw:
        print(i, end=' ')
    print()