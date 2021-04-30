import sys


def EuclidAlgGCD(a, b):
    
    #checks if inputs are valid.
    if (a < 0 or b < 0):
        sys.exit("ERROR: numbers must be non-negative")
    
    if (a == 0): 
        return b
    
    return EuclidAlgGCD(b%a, a)
    

def ExtendedEuclidAlgGCD(a, b):
    s=None
    t=None
    if (a < 0 or b < 0):
        sys.exit("ERROR: numbers must be non-negative")
        
    elif (a == 0):
        s = 0
        t = 1
        return (b), (s), (t)
    
    d, x1, y1 = ExtendedEuclidAlgGCD(b%a, a)
    
    s = y1 - (b//a)* x1
    t = x1
    
    return (d), (s), (t)


def ModArithmetic(a, n):
    if(n < 1):
        sys.exit("ERROR: N must be greater than 1")
    
    #Python3 uses true modulo, we do not need to check if value is negative
    d = a % n 
    return d


def RelativelyPrime(n):
    if (n <= 0 and n <=1):
        sys.exit("NO NUMBER WILL SATISFY THE RelativelyPrime conditions of " + str(n))

    ans = 1
    if n > 1:
        for i in range(2, n-1):
            if (EuclidAlgGCD(i,n)==1):
                ans = i
                break
        if ans == 1:
            for i in range(n+2, 3*n):
                if (EuclidAlgGCD(i,n)==1):
                    ans = i
                    break    
    
        return ans
    
def inverse(a, n):
    if (a < 0 or n <= 1):
        sys.exit("ERROR: invalid input for inverse")
    d, y, z = ExtendedEuclidAlgGCD(a, n)
    if (d == 1):
        return ModArithmetic(y, n)
    else:
        print("a and n are not relatively prime!")
        
def Encode(m, e, k):
    power = pow(m, e)
    return ModArithmetic(power, k)

def Decode(x, y, z):
    power= pow(x, y)
    return ModArithmetic(power, z)
    


p = int(input("Enter a Prime number (p): "))
while(p%2 == 0):
    print("This is not a prime number, try again!")
    p = int(input("Enter a Prime number (p): "))

q = int(input("Enter a different Prime number (q): "))
while(q%2 == 0 or q==p):
    if(q%2 == 0):
        print("This is not a prime number, try again!")
    if(q==p):
        print("This is the same as your previous, try again!")
    q = int(input("Enter a Prime number (q): "))


pq = (p*q)
print("p*q = ", pq)

phi = ((p-1)*(q-1)) 
# print("PHI: ", phi)

e = RelativelyPrime(phi) 
# print("E", e)

d = inverse(e, phi) 
# print("D", d)

M = int(input("Enter an integer smaller than " + str(pq) +": "))
while (M >= pq):
    print("This is not smaller than pq!")
    M = int(input("Enter an integer smaller than " + str(pq) +": "))

C = Encode(M, e, pq)
M1= Decode(C, d, pq)
    
if(M == M1):
    print("SUCCESS")
assert(M == M1)
