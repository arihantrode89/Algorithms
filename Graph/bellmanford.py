import sys

def relax(u,v,d):
    if d[v]>d[u]+w[u][v]:
        d[v]=d[u]+w[u][v]

def solution(d,V):
    for i in range(V):
        print(f'{i}---->{d[i]}')

def BellmanFord(V,src,w):
    d=[sys.maxsize]*V
    d[src]=0
    tupl=[(i,j) for i in  range(V) for j in range(V) if w[i][j]!=0]
    for _ in range(1,V):
        for (u,v) in tupl:
            relax(u,v,d)
    verification=True
    for (u,v) in tupl:
        if d[v]>d[u]+w[u][v]:
            verification=False

    if verification==True:
        solution(d,V)
    else:
        print("negative cycle exists")

if __name__=='__main__':
    Vertices=int(input("No.of vertices:"))
    w=[list(map(int,input().split(" "))) for j in range(5)] #you can also add any weights given to you instead of entering weight for each edge
    source=int(input("enter source:"))
    BellmanFord(Vertices,source,w)
        
