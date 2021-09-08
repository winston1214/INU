def isPerfect(a):
    s = 0
    i = 1
    while i <= a/2:
        if a % i == 0:
            s += i
        i+=1
    if s == a: return True
    else:
        return False

a = int(input('A : '))
if isPerfect(a): print('완전수입니다')
else:
    print('완전수가 아닙니다.')
