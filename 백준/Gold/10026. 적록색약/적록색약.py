import sys
sys.setrecursionlimit(10**6)

def Bdfs(x,y):
    if x<0 or y<0 or y>=n or x>=n:
        return False
    if graph[x][y]=='B':
        graph[x][y]='O'
        Bdfs(x-1,y)
        Bdfs(x+1,y)
        Bdfs(x,y-1)
        Bdfs(x,y+1)
        return True
    return False

def Rdfs(x,y):
    if x<0 or y<0 or y>=n or x>=n:
        return False
    if graph[x][y]=='R':
        graph[x][y]='Z'
        Rdfs(x-1,y)
        Rdfs(x+1,y)
        Rdfs(x,y-1)
        Rdfs(x,y+1)
        return True
    return False

def Gdfs(x,y):
    if x<0 or y<0 or y>=n or x>=n:
        return False
    if graph[x][y]=='G':
        graph[x][y]='Z'
        Gdfs(x-1,y)
        Gdfs(x+1,y)
        Gdfs(x,y-1)
        Gdfs(x,y+1)
        return True
    return False

def GRdfs(x,y):
    if x<0 or y<0 or y>=n or x>=n:
        return False
    if graph[x][y]=='Z':
        graph[x][y]='O'
        GRdfs(x-1,y)
        GRdfs(x+1,y)
        GRdfs(x,y-1)
        GRdfs(x,y+1)
        return True
    return False

graph=[]
n=int(input())
green=0
blue=0
red=0
rgreen=0

for i in range(n):
    graph.append(list(map(str,input())))

for i in range(n):
    for j in range(n):
        if Bdfs(i,j)==True:
            blue+=1
        if Rdfs(i,j)==True:
            red+=1
        if Gdfs(i,j)==True:
            green+=1

for i in range(n):
    for j in range(n):
        if GRdfs(i,j)==True:
            rgreen+=1

res=[red+green+blue,rgreen+blue]
for i in res:
    print(i,end=' ')