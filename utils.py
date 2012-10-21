import math,random
def saveToFile(l,fileName):
    ll = [str(x) for x in l]
    f = open(fileName,'w')
    f.write(','.join(ll))
    f.close()
    return

def loadFrmFile(fileName):
    for l in open(fileName):
        return [int(x) for x in l.strip().split(',')]

def isPal(s):
    if len(s)<2:
        return True
    if s[0]==s[-1]:
        return isPal(s[1:-1])
    return False


def getPrimes(n):
    if n<2: return []
##    if n==2: return [2]
    p = getPrimes(int(math.sqrt(n)))
    not_P = set([j for i in p for j in xrange(i*2,n,i)])
##    not_P = sorted([j for i in p for j in range(i*2,n,i)  if j not in locals()['_[1]']])
    p = [x for x in xrange(2,n+1) if x not in not_P]
    return p

def sumOfDigits(n):
    s=0
    while(n>0):
        s=s+(n%10)
        n=n/10
    return s


def isPrime(n):
    for i in xrange(1,5):
        a = random.randint(2,n)
        if not((a**(n-1))%n == 1):
            return False
    return True

def isPrime(n,ps):
    for p in ps:
        if p*p>n: break
        if n%p == 0:
            return False
    return True
