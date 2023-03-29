# 문제 조건 꼼꼼하게 읽고 풀면 됨
years = int(input())
if (years % 4 == 0 and years % 100 != 0) or years % 400 ==0:
    print(1)
else:
    print(0)