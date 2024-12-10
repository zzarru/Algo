T = 10
for test in range(1, T+1):
    N, pw = map(str, input().split()) # 숫자는 iterable하지 않기 때문에 str으로 받아준다.
    N = int(N) # N은 정수(int)로 변환해준다.

    stack = []
    for i in pw:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    print(f'#{test} {"".join(stack)}') # join메서드를 이용하여 문자열 리스트를 합쳐준다.