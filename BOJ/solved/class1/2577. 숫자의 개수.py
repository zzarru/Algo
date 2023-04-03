A = int(input())
B = int(input())
C = int(input())

nums = str(A*B*C)

num_lst = list(map(int, nums))

for i in range(10):
    print(num_lst.count(i))