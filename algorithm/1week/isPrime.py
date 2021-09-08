def isPrime(a):
    i = 2
    while i <= a/2:
        if a % i == 0:
            return '소수가 아닙니다'
        i+=1
    return '소수 입니다'
a = int(input('a = '))
print(isPrime(a))