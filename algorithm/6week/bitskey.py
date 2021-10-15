class bitskey:

    def __init__(self, x):

        self.x = x



    def get(self):

        return self.x



    def bits(self, k, j):

        return (self.x >> k) & ~(~0 << j)



a = int(input('a = '))

while a != 999:

    v = bitskey(a)

    for i in range(4, -1, -1):

        print(v.bits(i, 1), end='')

    print()

    a = int(input('a = '))