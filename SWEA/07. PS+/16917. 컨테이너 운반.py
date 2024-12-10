'''
stack의 pop을 이용한 문제 풀이
1) 컨테이너 오름차순 정렬, 트럭 내림차순 정렬
2) pop을 이용하여 가장 무거운 컨테이너 하차
3-1) 트럭에 적재할 수 있으면 싣고, 컨테이너 move 리스트에 넣어주기, truck의 idx +1
3-2) 적재할 수 없으면, 다음으로 무거운 컨테이너 하차
4) 컨테이너를 다 하차하거나 트럭이 하나도 남아있지 않을 때까지 반복
5) move list == 적재하여 옮긴 컨테이너의 합 구하기
'''

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    #1 정렬
    containers.sort() # 오름차순
    trucks.sort(reverse=True) # 내림차순

    #2 stack 이용해서 컨테이너 옮기기
    move = []
    idx = 0

    #4 옮길 컨테이너가 남아있지 않거나 트럭이 남아있지 않을 때까지
    while containers and idx < len(trucks):
        container = containers.pop()

        #3-1 화물 적재
        if container <= trucks[idx]:
            move.append(container)
            idx += 1

    #5 옮긴 컨테이너의 총 무게 합 구하기
    ans = sum(move)
    print(f'#{test} {ans}')
