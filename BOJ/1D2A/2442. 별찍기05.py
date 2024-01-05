N = int(input())
for n in range(1, N+1):
    if n != N:
        print(' '*(N-n)+'*'*(2*n-1)+' ')
    else:
        print(' '*(N-n)+'*'*(2*n-1))