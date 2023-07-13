M = int(input())

#1 총 사이클의 횟수를 구해야하므로 while문을 돌며 +1 해준다.
cycle = 0
#2 새로운 수를 업데이트 해주어야하기 때문에
N = M
#3 M은 0보다 같거나 큰 정수이므로 임의로 -1로 설정해주었다.
new_num = -1
while M != new_num:
    if N < 10:
        new_num = N*10 + N
    else:
        l = N%10
        r = N//10 + N%10
        if r < 10:
            new_num = l*10 + r
        else:
            new_num = l*10 + r%10

    cycle += 1
    N = new_num

print(cycle)