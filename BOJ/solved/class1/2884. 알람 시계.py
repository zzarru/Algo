#1 내 코드 (...이게 최선일까)
H , M = map(int, input().split())

alarm = (H*60 + M) - 45

alarm_H = alarm // 60
alarm_M = alarm % 60

if alarm_H <0:
    alarm_H = 24 + alarm_H

print(alarm_H, alarm_M)

'''
고려해야했던 tc
1) 0 30 -> 조건 없으면, -1 45 출력
2) if alarm_H ==0: 일 때, 0 -> 24로 바꿔줌
3) 0 45 -> 24 0 이 출력되는 불상사 발생..
'''

#2 입력된 M이 45(분) 보다 크거나 작을 때, 조건을 달리하여 출력하는 방법