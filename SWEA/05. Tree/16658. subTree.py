T = int(input())
for test in range(1, T+1):
    V, N = map(int, input().split())
    lst = list(map(int, input().split()))

    # 인접 리스트 만들어주기
    adjL = [[] for _ in range(max(lst)+1)] # 노드의 개수를 모르기 때문에 리스트의 max 값을 통해 노드 개수를 구한다.
    for i in range(V):
        P = lst[i*2] # 부모 노드
        C = lst[i*2 +1] # 자식 노드
        adjL[P].append(C)

    # visited 리스트 만들어주기
    visited = [0]*(max(lst)+1)

    # Queue 만들기
    Q = [N] # 시작 노드 일단 넣어주고 시작한다.
    while Q: # 큐가 빌 때까지 반복
        v = Q.pop(0)
        visited[v] = 1
        for i in adjL[v]:
            if visited[i] == 0:
                Q.append(i)

    ans = sum(visited)
    print(f'#{test} {ans}')