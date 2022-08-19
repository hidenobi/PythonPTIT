import math
import re


def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True  
def totalDigitNumber(n):
    digitNumber = 0
    while(n>0):
        digitNumber+=(n%10)
        n//=10
    return digitNumber
T = int(input())
for i in range(T):
    [a,b] = map(int,input().split())
    if(is_prime(totalDigitNumber(math.gcd(a,b)))): print("YES")
    else: print("NO")
    