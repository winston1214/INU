def encipher(p,n,pk):
    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        for _ in range(pk):
            b = t % n
            t = a * b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)
    return c

def encode(p):
    m = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a==32: a = 64
        a -= 64
        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else:
            m += str(a)
    return m

plainText = 'SAVE PRIVATE RYAN '
N = 3713
S = 97
P = 37
plainMessage = encode(plainText)
print('original : ',plainMessage)
cipherMessage = encipher(plainMessage,N,P)
print('encoding : ',cipherMessage)