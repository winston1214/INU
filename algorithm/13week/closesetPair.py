import geo as g
import math

class node:
    def __init__(self):
        self.p = g.point(max,max,'')
        self.next = None
def comp(t):
    if t_pass == 1:
        return t.p.x
    else:
        return t.p.y
def merge(a,b):
    c = z
    while True:
        if comp(a) < comp(b):
            c.next = a
            c = a
            a = a.next
        else:
            c.next = b
            c = b
            b = b.next
        if c == z: break
    c = z.next
    z.next = z
    return c

def check(p1,p2):
    global min,cp1,cp2
    if p1.y != z.p.y and p2.y != z.p.y:
        dist = math.sqrt((p1.x - p2.x) * (p1*x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))
        if dist < min:
            min = dist
            cp1 = p1
            cp2 = p2
    
def sort(c,N):
    if c.next == z: return c
    a = c
    for _ in range(2,(N//2)+1):
        c = c.next
    b = c.next
    c.next = z
    c = merge(sort(a,N//2),sort(b,N - (N//2)))

    if t_pass == 2:
        middle = b.p.x
        p1 = z.p
        p2 = z.p
        p3 = z.p
        p4 = z.p
        a = c
        while a != z:
            if math.fabs(a.p.x - middle) < min:
                check(a.p,p1)
                check(a.p,p2)
                check(a.p,p4)
                check(a.p,p4)
                p1 = p2
                p2 = p3
                p3 = p4
            a = a.next
    return c

def readlist():
    p = node()
    h = p
    for i in range(N):
        t = node()
        t.p.x = g.x_values[i]
        t.p.y = g.y_values[i]
        t.p.c = g.c_values[i]
        p.next = t
        p = p.next
    p.next = z
    return h
N = 16
max = 1000
cp1 = g.point(max,max,'')
cp2 = g.point(max,max,'')
min = max

z = node()
z.p.x = max
z.p.y = max
z.next = z
h = node()
h.next = readlist()

t_pass = 1
h.next = sort(h.next,N)
t_pass = 2
h.next = sort(h.next,N)

print('min = %.3f, cp1 = %s, cp2 = %s'%(min,cp1.c,cp2.c))