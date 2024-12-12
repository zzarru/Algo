#0 입력 받기
N = int(input()) # 참가자 수
shirts = list(map(int, input().split())) # 각 티셔츠 별 신청자 수
T, P = map(int, input().split()) # T=티셔츠 묶음 최소 주문 단위,  P=펜 묶음 최소 주문 단위

#1 티셔츠 묶음 주문 개수 구하기
order_shirts = 0
for shirt in shirts:
    if shirt % T != 0: # 나머지가 있으면 += 1
        order_shirts += (shirt // T + 1)
    else: # 나누어 떨어지면 몫만
        order_shirts += shirt // T

print(order_shirts)

#2 펜 묶음 및 낱개 주문 개수 구하기
pen_set = N // P
pen = N % P

print(pen_set, pen)