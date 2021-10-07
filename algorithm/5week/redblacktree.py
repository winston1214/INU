black = 0
red = 0

class node:
    def __init__(self,color,key=None,left=None,right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = q= gg= node
    z = node(color = black,key=0,left=0,right=0)
    z.left = z
    z.right = z
    head = node(color=black,key=0,left=0,right=z)

    def search(self,search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else: x = x.right
        return -1

    def insert(self,v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return 
            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)

        x = node(color=red, key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def check(self, search_key):
        x = p = self.head.right
        while (x != self.z):
            if x.color == 0:
                str_color = 'black'
            else:
                str_color = 'red'
            print('key : ', x.key, ', parents: ', p.key, ', color : ', str_color)
            p = x
            if x.key > search_key:
                x = x.left
            else:
                x = x.right

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black

        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = black
    
    def rotate(self,v,y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right
        if c.key > v:
            gc = c.left
            c.left = gc.right
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c
        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc
d = Dict()
key = int(input('키 : '))
while key != 999:
    d.insert(key)
    d.check(key)
    key = int(input('키 : '))