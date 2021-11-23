import geo as g

def theta(p1,p2):
    dx = p2.x - p1.x
    ax = abs(dx)
    dy = p2.y - p1.y
    ay = abs(dy)
    if ax + ay == 0:
        t = 0
    else:
        t = dy/(ax+ay)
    if dx < 0:
        t = 2-t
    elif dy < 0:
        t = 4+t
    return t * 90

def packageWarpping(p,n):
    minIndex = 0
    for i in range(n):
        if p[i].y < p[minIndex].y :
            minIndex = i
    p[n] = p[minIndex]
    th = 0.0
    for m in range(n):
        p[m],p[minIndex] = p[minIndex],p[m]
        minIndex = n
        v = th
        th = 360.0
        for i in range(m+1,n+1):
            if theta(p[m],p[i]) > v:
                if theta(p[m],p[i]) < th:
                    minIndex = i
                    th = theta(p[m],p[minIndex])
        if minIndex == n:
            return m
N = 16
p = []
for i in range(N):
    p.append(g.point(g.x_values[i],g.y_values[i],g.c_values[i]))
p.append(g.point(None,None,None))
M = packageWarpping(p,N)
for i in range(M+1):
    print(p[i].c,end = ' ')