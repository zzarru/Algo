def inorderTraverse(i):
    global cnt
    if 0 < i <= N:
        inorderTraverse(i*2)
        tree[i] = cnt
        cnt += 1
        inorderTraverse(i*2 + 1)


T = int(input())
for test in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1)
    cnt = 1 # 카운트 초기화를 밖에서 해줘야한다.

    inorderTraverse(1) # 트리 만들기~

    print(f'#{test} {tree[1]} {tree[N//2]}')