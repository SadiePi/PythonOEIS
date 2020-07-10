# OEIS.py (Author: Sadie Dotzler, github.com/jadotz)

# Implementation of the sequences in the Online Encyclopedia of Integer Sequences - oeis.org
# Functions labeled with 'A' will return the 'n'th integer in the sequence
# Functions labeled with 'G' will return a generator that will yield each element in the sequence up to 'limit'
# (This is done to abstract away optimizations to sequences that rely on previous elements such as the primes)
# For information on each sequence, see the associated OEIS page (e.g. oeis.org/A000040)

# Sequences are being implemented in order of increasing index, with the following exceptions
# Skipped sequences:
#  000001 - No full formula, subject not sufficiently understood
#  000003 - No full formula, subject not sufficiently understood
#  000009 - No understood formula, will look again later
# Preempted sequences: 
#  000040 - Primes, very useful
#  000115 - Used in 000008
#  000196 - Previously used in another sequence
#  005132 - Recaman's Sequence, just fun

# Utility functions for converting between A and G functions
def __G2A(g, n):
    for i in range(n-1):
        next(g)
    return next(g)

def __A2G(a, limit):
    n = 0
    while n < limit:
        yield a(n)
        n += 1

# number of groups of order n
def A000001(n):
    raise NotImplementedError("No full formula, subject not sufficiently understood")

def G000001(limit=float('inf')):
    yield from __A2G(A000001, limit)

# length of nth run in the sequence
def A000002(n):
    return __G2A(G000002, n)

def G000002(limit=float('inf')):
    ret = [1]
    yield 1
    read = start = n = 1
    while n < limit:
        ret.append(3 - ret[start - 1])
        yield ret[-1]
        n += 1
        if n - start >= ret[read]:
            read += 1
            start = len(ret)

# IDFK, see https://oeis.org/A000003
def A000003(n):
    raise NotImplementedError()

def G000003(limit=float('inf')):
    raise NotImplementedError()

# All the 0s
def A000004(n):
    return 0

def G000004(limit=float('inf')):
    yield from __A2G(A000004, limit)

# number of divisors of n
def A000005(n):
    prod = 1
    primes = G000040()
    for p in primes:
        if p > n:
            break
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        prod *= e+1
    return prod

def G000005(limit=float('inf')):
    yield from __A2G(A000005, limit)

# floor(sqrt(nth prime))
def A000006(n):
    from math import sqrt, floor
    return floor(sqrt(n))

def G000006(limit=float('inf')):
    yield from __A2G(A000006, limit)

# 1 then all the 0s
def A000007(n):
    return 0 if n else 1

def G000007(limit=float('inf')):
    yield from __A2G(A000007, limit)

# partitions of n into parts 1, 2, 5, 10
def A000008(n):
    from math import floor
    q = floor(n/10)
    h = A000115(n)
    # is always and int, round just to remove .0
    return round((q+1)*(h - q*(3*n-10*q+7)/6))

def G000008(limit=float('inf')):
    yield from __A2G(A000008, limit)

# number of partitions of n into odd parts
def A000009(n):
    raise NotImplementedError()

def G000009(limit=float('inf')):
    raise NotImplementedError()

# totient of n
def A000010(limit=float('inf')):
    from math import sqrt
    
    n = 1
    while n < limit:
        temp = n
        for p in G000040():
            if p > n:
                yield temp
                break
            if n % p == 0:
                temp = temp * (p-1) // p
        n += 1

def A000011(limit=float('inf')):
    raise NotImplementedError()


def A000013(limit=float('inf')):
    n = 0
    while n < limit:
        totg = A000010()
        s = 0
        for d in range(1, limit//2+1):
            tot2d = next(totg)
            next(totg)

            if n % d == 0:
                s += tot2d * pow(2, n//d) // 2*n
        yield s
        n += 1


# nth prime
def G000040(limit=float('inf')):
    if limit == 0:
        return
    ps = [2]
    yield 2
    n = 1
    c = 3
    while n < limit:
        if all(c % p for p in ps):
            ps.append(c)
            yield c
            n += 1
        c += 2

def A000115(n):
    from math import pow
    return round(pow(n+4, 2)/20)

def G000115(limit=float('inf')):
    yield from __A2G(A000115, limit)

def A000196(limit=float('inf')):
    from math import sqrt, floor
    
    n = 0
    while n < limit:
        yield floor(sqrt(n))
        n += 1

# recaman's sequence
def A005132(limit=float('inf')):
    if limit == 0:
        return
    ret = [0]
    yield 0
    n = 1
    while n < limit:
        if ret[-1]-n > 0 and ret[-1]-n not in ret:
            ret.append(ret[-1] - n)
        else:
            ret.append(ret[n-1] + n)
        yield ret[-1]
        n += 1



