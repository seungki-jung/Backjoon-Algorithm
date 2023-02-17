n,m = list(map(int,input().split()))
dic = {}
res = []

for i in range(n):
    a, b = list(map(str,input().split()))
    dic[a] = b

for p in range(m):
    res.append(input())

for ans in res:
    print(dic[ans])