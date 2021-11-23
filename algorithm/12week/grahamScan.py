import geo as g
def ccw(p0,p1,p2):
    dx1 = p1.x - p0.x
    dy1 = p1.y - p0.x
    dx2 = p2.x - p0.x
    dy2 = p2.y - p0.y
    if dx1 * dy2 > dy1 * dx2 : return 1
    if dx1 * dy2 < dy1 * dx2 : return -1
    if dx1 == 0 and dy1 == 0: return 0
    if dx1*dx2 < 0 or dy1*dy2 < 0 : return -1
    if dx1 * dx1 + dy1*dy1 < dx2*dx2 + dy2*dy2 : return 1
    return 0
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
def selectionSort(p,n):
    for i in range(1,n):
        minIndex = i
        for j in range(i+1,n+1):
            if theta(p[1],p[j]) < theta(p[1],p[minIndex]):
                minIndex = j
        p[minIndex],p[i] = p[i],p[minIndex]

def grahamScan(p,n):
    minIndex = 1
    for i in range(2,n+1):
        if p[i].y < p[minIndex].y:
            minIndex = i
    for i in range(1,n+1):
        if p[i].y == p[minIndex].y:
            if p[i].x > p[minIndex].x:
                minIndex = i
    p[1],p[minIndex] = p[minIndex],p[1]
    selectionSort(p,n)
    p[0] = p[n]
    m = 3
    for i in range(4,n+1):
        while ccw(p[m],p[m-1],p[i]) >= 0:
            m -= 1
        m+=1
        p[i],p[m] = p[m],p[i]
    return m

N = 16
p = []
p.append(g.point(0,0,None))
for i in range(N):
    p.append(g.point(g.x_values[i],g.y_values[i],g.c_values[i]))
M = grahamScan(p,N)
for i in range(1,M+1):
    print(p[i].c,end = ' ')