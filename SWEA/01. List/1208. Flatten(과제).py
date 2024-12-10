t = 10 # 테스트 케이스

for i in range(t):
    dump = int(input()) # 덤프횟수
    h = list(map(int, input().split())) # 박스 높이 리스트


    for j in range(dump):
        max_h = h.index(max(h))
        min_h = h.index(min(h))
        h[max_h] -= 1
        h[min_h] += 1

    print(f"#{i+1} {max(h) - min(h)}")