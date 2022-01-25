# counting number of bits
def countSetBits(n):
  count = 0
  while (n):
    count += n & 1
    n >>= 1
    # print(n, count, bin(n))
  return count

countSetBits(22)

# counting number of bits using diffrent approach
def countsetbits2(n):
  count = 0
  while n>0:
    n = n&(n-1)
    count+=1
  return count

countsetbits2(22)