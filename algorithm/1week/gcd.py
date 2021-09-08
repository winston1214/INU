def gcd(a,b):
    i = 1
    while i<=a and i<=b:
        if a%i == 0 and b%i == 0:
            g = i
        i += 1
    return g
A = int(input('a = '))
B = int(input('b = '))
print('GCD : ',gcd(A,B))