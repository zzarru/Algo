T = int(input())
for test in range(1, T+1):
    tc, N = map(str, input().split())
    N = int(N)
    lst = list(map(str, input().split()))

    gns_dic = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    gns_reversed_dic = {v:k for k,v in gns_dic.items()}

    gns_keys = []
    for i in lst:
        gns_keys.append(gns_dic.get(i))

    gns_keys.sort()

    ordered_lst = []
    for i in gns_keys:
        ordered_lst.append(gns_reversed_dic.get(i))

    print(f'{tc}', end=' ')
    for i in ordered_lst:
        print(i, end=' ')
    print()