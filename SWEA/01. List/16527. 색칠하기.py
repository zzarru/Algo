T = int(input())
 
for test in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    red = []
    for color in arr:
        if color[4] == 1:
            for i in range(color[0], color[2]+1):
                for j in range(color[1], color[3]+1):
                    red.append([i, j])
 
    blue = []
    for color in arr:
        if color[4] == 2:
            for i in range(color[0], color[2] + 1):
                for j in range(color[1], color[3] + 1):
                    blue.append([i, j])
    purple = []
    for r in red:
        if r in blue:
            purple.append(r)
 
    print(f'#{test+1} {len(purple)}')







    # 하드 코딩의 삶...
    # color_arr = []
    # for i in range(1, n+1):
    #     color_arr.append(list(map(int, input().split())))



