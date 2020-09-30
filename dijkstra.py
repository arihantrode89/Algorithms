import sys
from time import time
def minimum(dist,V,S):
    # global vertices,d,Pi
    minn=sys.maxsize
    for v in range(V):
        if dist[v]<minn and S[v]==False:
            minn=dist[v]
            min_indexx=v
    return min_indexx
           
def relax(u,v,d):
    # global w,d,Pi
    if d[v]>d[u]+w[u][v]:
        d[v]=d[u]+w[u][v]
        # Pi[v]=u

def solution(d,V):
    for i in range(V):
        print(f'{i}--->{d[i]}')
    
def Dijkstra(src,V):
    t=time()
    d=[sys.maxsize]*V
    d[src]=0
    S=[False]*V
    
    for _ in range(V):
        u=minimum(d,V,S)
        S[u]=True
        for v in range(V):
            if w[u][v]>0 and S[v]==False:
                relax(u,v,d)
    solution(d,V)
    print(f'{time()-t}')

if __name__=='__main__':
    vertices=int(input('Enter No. vertices:'))
    w=[[0,10,3,0,0],[0,0,1,2,0],[0,4,0,8,2],[0,0,0,0,7],[0,0,0,9,0]]
    source=int(input('Source:'))
    Dijkstra(source,vertices)
