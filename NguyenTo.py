import math

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

T = int(input())
for t in range(T):
    n = int(input())
    count = 1
    for i in range(2,n):
        if(math.gcd(i,n)==1): count+=1
    if is_prime(count): print("YES")
    else: print("NO")
