#1 내가 제출한 코드 (이게 맞나..)
x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)
list = [x, y, (w-x), (h-y)]
print(min(list))

#2 map 어케 쓰는 건데..! 리스트 요소로 넣을 때 쓰는 거라매....감자는 혼란스럽다.
x, y, w, h = map(int, input().split())
print(min(x, y, (w-x), (h-y)))