# tree 만들어서 탐색 순서 알아내기
def inorderTraverse(i):
    global cnt
    if 0 < i <= N:
        inorderTraverse(i*2)
        tree[i] = cnt
        cnt += 1
        inorderTraverse(i*2 + 1)

T = 1
for test in range(1, 11):
    N = int(input())
    lst = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        letters = list(input().split())
        lst[i] = letters

    tree = [0] *(N+1)
    cnt = 1
    inorderTraverse(1)

    word = [[] for _ in range(N)]
    for j in range(1, N+1):
        idx = tree[j]
        word[idx-1] = lst[j][1]

    print(f'#{test} {"".join(map(str, word))}')