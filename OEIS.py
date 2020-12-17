from math import floor, sqrt
# OEIS.py (Author: Sadie Dotzler, github.com/jadotz)

# Implementation of the sequences in the Online Encyclopedia of Integer Sequences - oeis.org
# Functions labeled with 'A' will return the 'n'th integer in the sequence
# Functions labeled with 'G' will return a generator that will yield each element in the sequence up to 'limit'
# (This is done to abstract away optimizations to sequences that rely on previous elements such as the primes)
# For information on each sequence, see the associated OEIS page (e.g. oeis.org/A000040)
# Once many more sequences are implemented, I'll be refactoring many of them to use crossref formulas,
#  hopefully simplifying them

# Sequences are being implemented in order of increasing index, with the following exceptions
# Skipped sequences:
#  000001 - No full formula, subject not sufficiently understood
#  000003 - No full formula, subject not sufficiently understood
#  000009 - No understood formula, will look again later
#  000014 - No full formula, subject not sufficiently understood
# Preempted sequences: 
#  000040 - Primes, very useful
#  000115 - Used in 000008
#  000196 - Previously used in another sequence
#  005132 - Recaman's Sequence, just fun

# Utility functions for converting between A and G functions
# For when the best way to implement one is to just use the other
def __G2A(g, n):
    for _ in range(n-1):
        next(g)
    return next(g)

def __A2G(a, limit, offset):
    n = offset
    while n < limit:
        yield a(n)
        n += 1

# number of groups of order n
def A000001(n):
    raise NotImplementedError()

def G000001(limit=float('inf')):
    raise NotImplementedError()

# length of nth run in the sequence
def A000002(n):
    return __G2A(G000002(), n)

def G000002(limit=float('inf')):
    x = y = -1
    i = 0
    while i < limit:
        yield [2, 1][x&1]
        f = y &~ (y+1)
        x ^= f
        y = (y+1) | (f & (x>>1))
# my own much worse implementation
# def G000002(limit=float('inf')):
#     ret = [1]
#     yield 1
#     read = start = n = 1
#     while n < limit:
#         ret.append(3 - ret[start - 1])
#         yield ret[-1]
#         n += 1
#         if n - start >= ret[read]:
#             read += 1
#             start = len(ret)

# IDFK, see https://oeis.org/A000003
def A000003(n):
    raise NotImplementedError()

def G000003(limit=float('inf')):
    raise NotImplementedError()

# All the 0s
def A000004(n):
    return 0

def G000004(limit=float('inf')):
    yield from __A2G(A000004, limit, 0)

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
    yield from __A2G(A000005, limit, 1)

# floor(sqrt(nth prime))
def A000006(n):
    return floor(sqrt(A000040(n)))

def G000006(limit=float('inf')):
    primes = G000040()
    n = 1
    while n < limit:
        yield floor(sqrt(next(primes)))

# 1 then all the 0s
def A000007(n):
    return 0 if n else 1

def G000007(limit=float('inf')):
    yield from __A2G(A000007, limit, 0)

# partitions of n into parts 1, 2, 5, 10
def A000008(n):
    q = floor(n/10)
    h = A000115(n)
    # is always and int, round just to remove .0
    return round((q+1)*(h - q*(3*n-10*q+7)/6))

def G000008(limit=float('inf')):
    yield from __A2G(A000008, limit, 0)

# number of partitions of n into odd parts
def A000009(n):
    raise NotImplementedError()

def G000009(limit=float('inf')):
    raise NotImplementedError()

# totient of n
def A000010(n):
    temp = n
    for p in G000040():
        if p > n:
            return temp
        if n % p == 0:
            temp = temp * (p-1) // p

def G000010(limit=float('inf')):
    yield from __A2G(A000010, limit, 1)

def A000011(n):
    return (A000013(n) + 2**(n//2))//2

def G000011(limit=float('inf')):
    yield from __A2G(A000011, limit, 0)

def A000012(n):
    return 1

def G000012(limit=float('inf')):
    yield from __A2G(A000012, limit, 0)

def A000013(n):
    return round(sum(A000010(2*d)*2**(n//d)/(2*n) for d in range(1, n+1) if n%d==0)) if n>0 else 1

def G000013(limit=float('inf')):
    yield from __A2G(A000013, limit, 0)

def A000014(n):
    raise NotImplementedError()

def G000014(limit=float('inf')):
    raise NotImplementedError()

def A000015(n):
    # I'm not happy with this but it works
    primes = list(G000040(n))
    powers = [1]
    for k in range(1, n.bit_length()+1):
        powers += [p**k for p in primes]
    powers.sort()
    for p in powers:
        if p >= n:
            return p

def G000015(limit=float('inf')):
    yield from __A2G(A000015, limit, 1)

def A000016(n):
    return round(sum(A000010(d)*2**(n//d)/(2*n) for d in range(1, n+1, 2) if n%d==0)) if n>0 else 1

def G000016(limit=float('inf')):
    yield from __A2G(A000016, limit, 0)


def A000017(n):
    return [-1, 1, 0, 0, 2, 2, 4, 8, 4, 16, 12, 48, 80, 136, 420, 1240, 2872, 7652, 18104, 50184][n] if n < 19 else -1

def G000017(limit=float('inf')):
    yield from __A2G(A000017, limit, 1)






# nth prime
def A000040(n):
    return __G2A(G000040(), n)

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
    return (n+4)**2//20

def G000115(limit=float('inf')):
    yield from __A2G(A000115, limit, 0)

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



