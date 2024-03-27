def familyship(P1, P2):
    # P1부터 시작한다.
    stack = [P1]
    v = stack.pop()
    if not visited[v]:
        visited[v] = True

        total = 0
        cnt = 0
        for i in range(len(family[v])):
            if family[v][i] == 1 and not visited[i]:
                if i == P2:
                    return total - cnt
                stack.append(i)
                total += 1
            elif family[v][i] == 1 and visited[i]:
                total += 1
                cnt += 1


N = int(input())
P1, P2 = map(int, input().split())
M = int(input())

family = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

# 가족 관계도(2차원리스트; 인접행렬)
for _ in range(M):
    x, y = map(int, input().split())
    family[x][y] = family[y][x] = 1

print(familyship(P1, P2))