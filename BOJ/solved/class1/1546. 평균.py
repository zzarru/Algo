#1 내가 제출한 코드
N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_scores = []
for score in scores:
    new_scores.append(score/M*100)

average = sum(new_scores) / N

print(average)

#2 다른 코드
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

for i in range(N):
    scores[i] = scores[i]/M *100

average = sum(scores) / N

print(average)

