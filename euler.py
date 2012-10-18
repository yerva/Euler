####INF = 100000
####
####dp=[]
####for i in xrange(0,21):
####    dp.append([INF]*21)
####
####dp[20][20]=1
####
####def DP(i,j):
####    if i>20 or j>20:
####        return 0
####    if dp[i][j] != INF:
####        return dp[i][j]
####
####    dp[i][j] = DP(i+1,j)+DP(i,j+1)
####    return dp[i][j]
####
####print DP(0,0)
##
import math
def Primes(N):
    s = set()
    i = 1
    while i<N+1:
        i=i+1
        isP=True
        for p in s:
            if i%p == 0:
                isP=False
                break
        if isP:
            s.add(i)
    return sorted(s)


##Ps = Primes(10000)
##def getPFact(n):
##    for p in Ps:
##        if n%p == 0:
##            return p
##    return n
##
##def getPFactors(n):
##    pfs = dict()
##    while n!=1:
##        p = getPFact(n)
##        n = n/p
##        if not pfs.has_key(p):
##            pfs[p] = 0
##        pfs[p] = pfs[p] + 1
##
##    ans = 1
##    for k in pfs.keys():
##        ans = ans*(1+pfs[k])
##    return ans
##    
##
##on = 2
##of = 2
##mx = 1
##while 1==1:
##    nn = on+1
##    nf = getPFactors(nn)
##    if mx < nf*of:
##        mx = nf*of
##        print [nn, nf, nf*of]
##    if nf*of > 600:
##        break
##    on = nn
##    of = nf
##
###print getPFactors(2079*1040)
##
##def nfac(n):
##    ans = 1
##    for x in xrange(2,n+1):
##        if n%x == 0:
##            ans = ans+1
##    return ans
##
####x=3000
####mx = 1
####while (1==1):
####    x=x+1
####    n = x*(x+1)/2
####    nf = getPFactors(n)
####    if nf > mx:
####        mx = nf
####        print [nf,x]
####    if nf>500:
####        print x
####        break

##a=[0]*10000
##def getN(n):
##    s = 0
##    while n!= 1:
##        if n<10000 and a[n] != 0:
##            s = s + a[n]
##            break
##        s = s+1
##        if n%2==0:
##            n = n/2
##        else:
##            n = 3*n + 1
##
##    if n<10000:
##        a[n] = s
##    return s
##
##mx = 1
##ans = 1
##for i in xrange(2,1000001):
##    nn = getN(i)
##    if mx < nn:
##        print [i,nn]
##        mx = nn
##        ans = i
##print ans

##a=[[75],
##[95,64],
##[17,47,82],
##[18,35,87,10],
##[20,04,82,47,65],
##[19,01,23,75,03,34],
##[88,02,77,73,07,63,67],
##[99,65,04,28,06,16,70,92],
##[41,41,26,56,83,40,80,70,33],
##[41,48,72,33,47,32,37,16,94,29],
##[53,71,44,65,25,43,91,52,97,51,14],
##[70,11,33,28,77,73,17,78,39,68,17,57],
##[91,71,52,38,17,14,91,43,58,50,27,29,48],
##[63,66,04,68,89,53,67,30,73,16,69,87,40,31],
##[04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]]
##
##def mxsum(a,b):
##    return [ max(a[i]+b[i],a[i]+b[i+1]) for i in xrange(0,len(a))]
##
##
##nn =[]
##nn = a[-1]
##for i in xrange(len(a)-2,-1,-1):
##             nn = mxsum(a[i],nn)
##print nn
##             
##

##
##c=0
##ans=''
##def doPerm(soFar, rem):
##    #print soFar+':'+'.'.join([str(x) for x in rem])
##    global c
##    global ans
##    #print rem
##    if len(rem) == 0 :
##        c = c+1
##        if c%100000 == 0:
##            print soFar
##        if (c==1000000):
##            ans=soFar
##            print soFar
##        return
##    for i in rem:
##        l = list(rem)
##     #   print l
##        l.remove(i)
##      #  print l
##        doPerm(soFar+str(i),l)
##               
##    return
##
##print 'started'
##doPerm("",range(0,10))
##print ans
##print 'finshed'        
        
##a=[]
##i=1
##s=0
##line=''
##for l in open('names.txt'):
##    #print l
##    line = l
##ll = line.split(',')
##sl = sorted(ll)
##    
##for l in sl:
##    sm = 0
##    for c in l.replace('"','').strip():
##        #print c
##        sm = sm+ord(c)-ord('A')+1
##    s = s+i*sm
##    if i == 938:
##        print l
##        print [i,sm,i*sm]
##    i = i+1

##INF = -1
##a=[]
##for l in open('matrix.txt'):
##    a.append([int(x) for x in l.strip().split(',')])
##b=[]
##for i in xrange(0,80):
##    b.append([-1]*80)
##
##b[79][79] = a[79][79]
##
##def dp(i,j):
##    if i>79 or j>79:
##        return 9999999
##    if b[i][j] != INF:
##        return b[i][j]
##    ans = a[i][j]+min(dp(i+1,j),dp(i,j+1))
##    b[i][j] = ans
##    return ans
##
##a = dp(0,0)
##print a

##mx = 0
##ans = 0
##Ps = Primes(1000)
##PSS = Primes(100000)
##for a in xrange(-999,1000):
##    for b in Ps:
##        cnt = 0
##        for n in xrange(0,1000):
##            if n*n+a*n+b in PSS:
##                cnt = cnt+1
##            else:
##                break
##        if a==1 and b==41:
##            print [cnt,a,b,a*b]
##        if mx < cnt:
##            mx=cnt
##            ans = a*b
##            print [mx,a,b,a*b]
##print ans

##PSS = Primes(100000)
##def gcd(a,b):
##    if a==0:
##        return b
##    if a==b:
##        return a
##    if a>b:
##        return gcd(a%b,b)
##    else:
##        return gcd(b%a,a)
##n=70968
##MIN=1
##while 1==1:
##    n=n+1
##    b=n-1
##    a=0
##    if n in PSS:
##        continue
##    for i in xrange(1,n):
##        if gcd(i,n)==1:
##            a=a+1
##    if MIN>(a+0.0)/b:
##        MIN = (a+0.0)/b
##        print ['*******',n,(a+0.0)/b,15499.0/94744]
##    if n%1000 == 0:
##        print [n,(a+0.0)/b,15499.0/94744]
##    if (a+0.0)/b < (15499.0/94744):
##        print n
##        break

##amicable numbers
##def getS(n):
##    sm = 0
##    for f in xrange(1,(n+3)/2):
##        if n%f == 0:
##            sm = sm + f
##    return sm
##a = set()
##for i in xrange(1,21824):
##    if getS(i) > i:
##        a.add(i)
##
##a=sorted(a)
##b=set()
##for x in a:
##    for y in a:
##        if (x+y)<21824:
##            b.add(x+y)
##print 'done'
##



##a=dict()
##a[1] = 0
##a1=0
##for n in xrange(2,10000):
##    if a.has_key(n):
##        continue
##    sm = getS(n)
##    smsm = getS(sm)
##    a[n] = sm
##    if smsm < 10000:
##        a[sm] = smsm
##    if n == smsm and n!=sm:
##        print str(n)+"->"+str(sm)+"->"+str(smsm)
##        a1 = a1+n
##        if sm < 10000:
##            a1=a1+sm
####ans = 0
####for n in xrange(2,10000):
####    print [n,a[n]]
####    if a[n] != n and a[a[n]] == n:
####        ans = ans+n
##print a1
                    
##def rec(s):
##    for i in xrange(6,1000):
##        if s[0:i] == s[i:2*i]:
##            return i
##       
##from decimal import *
##def drec(n):
##    d = Decimal(1) / Decimal(n)
##    return rec(str(d).split('.')[1])
##ans=0
##dans = 0
##getcontext().prec = 2000
##for d in xrange(2,1000):
##    n = drec(d)
##    print [d,n]
##    if ans < n:
##        ans = n
##        dans = d
##print 'done'
##print dans

##def nsq(n):
##    if n==1:
##        return 1
##    return 4*n*n-6*n+6
##
##sm = 0
##for n in xrange(1,1002,2):
##    sm = sm +nsq(n)
##print sm

##s=set()
##for a in xrange(2,101):
##    for b in xrange(2,101):
##        s.add(a**b)
##print len(s)

##def s(n,a):
##    return sum([int(x)**a for x in str(n)])
##
##sm=0
##for i in xrange(2,1000000):
##    if i == s(i,5):
##        sm = sm + i
##        print i
##print sm

##a=sum([x**x for x in xrange(1,1001)])

##def isPal(s):
##    if len(s)<2:
##        return True
##    if s[0]==s[-1]:
##        return isPal(s[1:-1])
##    return False
##
##sm=0
##for n in xrange(1,1000001):
##    if isPal(str(n)) and isPal(bin(n)[2:]):
##        print [n,bin(n)]
##        sm=sm+n
##print sm

##def mod(x,y):
##    sx = set(str(x))
##    sy = set(str(y))
##    sxy = sx.union(sy)
##    if len(sxy)==3:
##        xd = [int(x) for x in sxy.difference(sy)]
##        yd = [int(x) for x in sxy.difference(sx)]
##        return [xd[0],yd[0]]
##    return []
##
##def areEq(x,y):
##    d = mod(x,y)
##    if len(d)==0:
##        return False
##    return x*d[1]==y*d[0]
##    
##n = 1
##d = 1
##for x in xrange(11,100):
##    for y in xrange(x+1,100):
##        if x==y or x%10 == 0 or y%10==0:
##            continue
##        if areEq(x,y):
##            [xd,yd]=mod(x,y)
##            print [x,y,'--',xd,yd]
##            n = n*xd
##            d = d*yd
##print [n,d]
            
def fac(n):
    if n<2:
        return 1
    return n*fac(n-1)


##def sf(n):
##    a=[fac(int(x)) for x in str(n)]
##    return sum(a)
##
##sm = 0
##for x in xrange(3,1000000):
##    if x==sf(x):
##        print x
##        sm = sm + x

##PS = Primes(1000000)
##A=[]
##for p in PS:
####    if len(str(p))==1:
####        break
##    isR = True
##    for l in xrange(1,len(str(p))):
##        a = str(p)
##        b = a[l:]+a[0:l]
##        if not int(b) in PS:
##            isR = False
##            break
##    if isR:
##        A.append(p)
##        print p
##print len(A)

##A=set()
##for x in xrange(1,100000):
##    if '0' in  str(x):
##        continue
##    for y in xrange(x,100000):
##        if '0' in  str(y):
##            continue
##        p = x*y
##        if '0' in  str(p):
##            continue
##        if sum([len(str(i)) for i in [x,y,p]]) != 9:
##            if sum([len(str(i)) for i in [x,y,p]]) > 9:
##                break
##            continue
##        [sx,sy,sp] = [set(str(i)) for i in [x,y,p]]
##        sxyp = sx.union(sy).union(sp)
##        if len(sxyp)==9:
##            A.add(p)
##            print [x,y,p,'**',len(A)]
##sm = sum(A)
##print sm

##A = []
##PS = Primes(1000000)
##for p in PS:
##    if p<10:
##        continue
##    sp = str(p)
##    l = len(str(p))
##
##    isT = True
##    for i in xrange(1,l+1):
##        if not (int(sp[0:i])) in PS:
##            isT = False
##            break
##        if not (int(sp[i-1:l])) in PS:
##            isT = False
##            break
##    if isT:
##        A.append(p)
##        print p

##B=[]
##for x  in xrange(191,100000):
##    s=""
##    for n in xrange(1,4):
##        sp = str(x*n)
##        if '0' in sp:
##            continue
##        s = s+sp
##        if len(s) == 9:
##            sq=sorted(set(s))
##            if len(sq)==9:
##                print str(x)+"****"+str(n)
##                print sq
##                B.append(int(s))
##                break
##print max(B)

##A=[0]*1001
##for a in xrange(1,1000):
##    for b in xrange(a,1000-a+1):
##        for c in xrange(b,1000-a-b+1):
##            if c*c == a*a+b*b:
##                print [a,b,c]
##                if (a+b+c) <= 1000:
##                    A[a+b+c] = A[a+b+c] + 1
##                else:
##                    break
##print max(A)

##A = [1,10,100,1000,10000,100000,1000000]
###A = range(1,20)
##i=1
##l = 0
##while i<1000000:
##    sn = str(i)
##    i = i+1
##    for x in sn:
##        l = l+1
##        if l in A:
##            print [l,x]

##PS = Primes(1000000)
##mx = 0
##ans = 0
##for p in PS:
##    ls = len(set(str(p)))
##    if(len(set(str(p))) >= mx and len(set([int(x) for x in str(p)]).difference(set(range(1,ls+1))))==0 and len([int(x) for x in str(p)])==len(set([int(x) for x in str(p)]))):
##        ans = p
##        mx = len(set(str(p)))
##        print [p,len(set(str(p)))]

##nn = []
##for n in xrange(1,21):
##    nn.append(n*(n+1)/2)
##
##def wn(s):
##    sm = 0
##    for x in s:
##        sm = sm + ord(x) - ord('A')+1
##    return sm
##
##for l in open('words.txt'):
##    a=[wn(s) for s in l.strip().replace('"','').split(',')]
##
##print max(a)
##ans = 0
##for x in a:
##    if x in nn:
##        ans=ans+1
##print ans

##def val(s):
##    return int(s[1:4])%2==0 and int(s[2:5])%3==0 and int(s[3:6])%5==0 and int(s[4:7])%7==0 and int(s[5:8])%11==0  and int(s[6:9])%13==0  and int(s[7:10])%17==0
##
##sm = 0
##def perm(soFar,rem):
##    global sm
##    if len(soFar) == 10:
##        if val(soFar):
##            sm = sm+int(soFar)
##            print soFar
##        return
##    for i in rem:
##        l = list(rem)
##        l.remove(i)
##        perm(soFar+str(i),l)
##
##perm('',range(0,10))

##P = []
##for n in xrange(1,10000):
##    P.append(n*(3*n-1)/2)
##mx = 10000000000
##for i in xrange(0,len(P)):
##    for j in xrange(i+1,len(P)):
##        if P[i]+P[j] in P and P[j]-P[i] in P:
##            print [P[i],P[j],P[j]-P[i]]
##            if mx > P[j]-P[i]:
##                mx = P[j]-P[i]
##                print mx
##print mx

##def Pn(n):
##    return n*(3*n-1)/2
##def Hn(n):
##    return n*(2*n-1)
##
##p=2
##h=5
##n=166
##m=143
##while not p==h:
##    if p > h:
##       m = m+1
##       h=Hn(m)
##    elif p<h :
##        n=n+1
##        p=Pn(n)
##    
##    
##print [p,h]

##import math
##PS = Primes(10000)
##
##for n in xrange(3,10001,2):
##    if n in PS:
##        continue
##    isG = True
##    for p in PS:
##        if p==2:
##            continue
##        if p>n:
##            break
##        d = (n-p)/2
##        sq = int(math.sqrt(d))
##        if sq*sq == d :
##            print [n,p,2*sq*sq, p+2*sq*sq]
##            isG = False
##            break
##    if isG:
##        print n
##        break

##Ps = Primes(1000)
##def getPFact(n):
##    for p in Ps:
##        if n%p == 0:
##            return p
##    return n
##
##def getPFactors(n):
##    pfs = set()
##    while n!=1:
##        p = getPFact(n)
##        n = n/p
##        pfs.add(p)
##    return pfs
##
##NN=3
##for i in xrange(10,10000000):
##    if i in Ps:
##        continue
##    if len(getPFactors(i))>=NN:
##        print [i,getPFactors(i)]
##        if len(getPFactors(i))>=NN and len(getPFactors(i+1))>=NN  and len(getPFactors(i+2))>=NN  and len(getPFactors(i+3))>=NN:
##            print [i,i+1,i+2,i+3]
##            break

##PS = [x for x in Primes(10000) if x>1000]
##def areSame(A,B):
##    sa = sorted(str(A))
##    sb = sorted(str(B))
##    return sa==sb
##for a in xrange(0,len(PS)):
##    for b in xrange(a+1,len(PS)):
##        for c in xrange(b+1,len(PS)):
##            if 2*PS[b]==PS[a]+PS[c] and areSame(PS[a],PS[b])  and areSame(PS[a],PS[c]):
##                print [PS[a],PS[b],PS[c]]

###*********************************************
##def saveToFile(l,fileName):
##    ll = [str(x) for x in l]
##    f = open(fileName,'w')
##    f.write(','.join(ll))
##    f.close()
##    return

##saveToFile(PS,'millionPrimes.txt')

def loadFrmFile(fileName):
    for l in open(fileName):
        return [int(x) for x in l.strip().split(',')]
###*********************************************

##PS = list(Primes(1000000))
PS = loadFrmFile('millionPrimes.txt')
##mn = 0
##ans = 0
##for j in xrange(0,len(PS)):
##    sm = 0
##    for i in xrange(j,len(PS)):
##        k = i-j+1
##        sm = sm+PS[i]
##        if sm in PS:
##            #print [k,sm]
##            if mn<=k:
##                mn=k
##                ans=sm
##                print [k,sm,'*******']
##        if sm>1000000:
##            break;

##def isPrime(n):
##    for p in PS:
##        if n%p == 0 :
##            return False
##        if p*p > n+1:
##            break
##    return True
##
##def perm(soFar,rem):
##    if len(soFar) == 7:
##        if isPrime(int(soFar)):
##            print soFar
##            return
##    for i in rem:
##        l = list(rem)
##        l.remove(i)
##        perm(soFar+i,l)
##    return
##
##perm('',[str(x) for x in range(1,8)])
##
####for p in PS:
####    sp = sorted(str(p))
####    ps = [str(x) for x in range(1,len(sp)+1)]
####    if ps == sp:
####        print p
ans=0
##for a in xrange(0,201):
##    for b in xrange(0,101):
##        for c in xrange(0,41):
##            for d in xrange(0,21):
##                for e in xrange(0,11):
##                    for f in xrange(0,5):
##                        for g in xrange(0,3):
##                            for h in xrange(0,2):
##                                if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h == 200:
##                                    ans = ans+1
####                                    print [a,b,ans]
##[a,b,c,d,e,f,g,h]=[0]*8
##for h in xrange(0,2):
##    if 200*h > 200:
##        break
##    for g in xrange(0,3):
##        if 100*g+200*h > 200:
##            break
##        for f in xrange(0,5):
##            if 50*f+100*g+200*h > 200:
##                break
##            for e in xrange(0,11):
##                if 20*e+50*f+100*g+200*h > 200:
##                    break
##                for d in xrange(0,21):
##                    if 10*d+20*e+50*f+100*g+200*h > 200:
##                        break
##                    for c in xrange(0,41):
##                        if 5*c+10*d+20*e+50*f+100*g+200*h > 200:
##                            break
##                        for b in xrange(0,101):
##                            if 2*b+5*c+10*d+20*e+50*f+100*g+200*h > 200:
##                                break
##                            ans = ans+1
##                            print [b,c,d,e,f,g,h,'**',ans]
####                            for a in xrange(0,201):
####                                if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h > 200:
####                                    break
####                                if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h == 200:
####                                    ans = ans+1
####                                    print [a,b,c,d,e,f,g,h,'**',ans]
##        
##print ans
##A=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
##C=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
##
##S=""
##for n in xrange(1,1000):
##    s=""
##    k = n
##    if n/100 > 0:
##        s = str(A[n/100-1])+" hundred"
##        if n%100 > 0:
##            s=s+" and "
##        k = n%100
##    if k<20 and k>0:
##        s = s+" "+A[k-1]
##    elif k>=20:
##        s = s + " "+ C[k/10-2]
##        k = k%10
##        if k>0:
##            s = s+" "+A[k-1]
##    S=S+s.replace(' ','')
##    print [n,s]
##S=S+"OneThousand"
##print len(S)

def memoize(f):
    memo = {}
    def helper(a,x):
        if (a,x) not in memo:            
            memo[(a,x)] = f(a,x)
        return memo[(a,x)]
    return helper
       
@memoize
def powr(a,x):
    if x==0: return 1
    if x==1: return a
    y = pow(a,x/2)%250
    if x%2==0:
        return (y*y)%250
    return (y*a*y)%250
        
a=[]
for i in xrange(1,250251):
    if(i%10000==0): print i
    x = i%250
    a.append(powr(x,i))
