#Reverse the array

a = [1,2,3,4,5,6]

# method1
print(a[::-1])

# method2
a.reverse()
print(a)

# method3
for i in range(len(a)//2):
  a[i],a[-i-1] = a[-i-1] , a[i]
print(a)

# method4
def rlist(liste,a,b):
  if a < len(liste)//2:
    liste[a], liste[b] = liste[b], liste[a]
    a,b = a+1,b-1
    return rlist(liste,a,b)
  else:
    return liste

b = rlist(a,0,-1)
print(b)
print(a)



# Find the maximum and minimum element in an array
import time
a = [2,1,3,5,7,5,4,54,3,5,67,0]
def minmax(a):
  a1 = a[0]
  b1 = a[0]
  for i in range(0, len(a)):
    if a[i]>a1:
      a1 = a[i]
    if a[i]<b1:
      b1 = a[i]
  return ("max =",a1,"min =",b1)
%timeit minmax(a)

# method 2
def minmax2(a):
  return("max =",max(a), "min =",min(a))
# %timeit minmax2(a)

# method 3
def minmax3(a):
  a.sort()
  return ("max =",a[-1],"min =",a[0])
# %timeit minmax3(a)



# Find the "Kth" max and min element of an array
a = [2,1,3,5,7,5,4,54,3,5,67,0]
def kthmaxmin(a,k):
  a.sort()
  return a[k-1],a[-k]

# %timeit kthmaxmin(a,2)


# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
a = [1,1,2,0,0,1,0,2,1,0,2,1,0,0,0,0]
j = len(a)-1
i = 0
k = 0
while i<=j :
  if a[i]==2 :
    a[i] ,a[j] = a[j], a[i]
    j-=1
    i-=1
  if a[i] == 0:
    a[i], a[k] = a[k], a[i]
    i-=1
    k+=1

  i+=1
print(a)


# Move all the negative elements to one side of the array
a = [-1,3,2,-5,6,-3,4,-3,-3,-3,-3,-3,-3]

i = 0
j = len(a)-1

while i<=j:
  if a[i] < 0:
    a[i],a[j] = a[j], a[i]
    j-=1
    i-=1
  i+=1

print(a)

# Find the Union and Intersection of the two sorted arrays.
a = [1,2,3,4,5,6,7]
b = [-2, -1,4,5,6,7,8,9]

#union
def union(a,b):
  i = 0
  j = 0
  c = []
  while True:
      if i == len(a) and j == len(b):
        break
      elif i != len(a) and j == len(b):
        c.append(a[i])
        i+=1
        continue
      elif i == len(a) and j != len(b):
        c.append(b[j])
        j+=1
        continue

      if a[i]< b[j]:
        c.append(a[i])
        i+=1

      elif a[i]> b[j]:
        c.append(b[j])
        j+=1

      elif a[i] == b[j]:
        c.append(b[j])
        i+=1
        j+=1
      # print(i,j)
  return c

print(union(a,b))

#intersection
def intersection(a,b):
  i = 0
  j = 0
  c = []
  while i!= len(a) and j!= len(b):
    if a[i] == b[j]:
      c.append(a[i])
      i+=1
      j+=1
    elif a[i] < b[j]:
      i+=1
    elif a[i] > b[j]:
      j+=1
  return c
print(intersection(a,b))
# %timeit intersection(a,b)

# Write a program to cyclically rotate an array by one.
a = [1,2,3,4,5,6]

def rotate(a,r):
  b = []
  print(r%len(a))
  for i in range(len(a)-1,-1,-1):
    b = [a[i-r%len(a)]]+b
  return b

# changing the original array
def rotate(arr, n):
  b = arr[0]
  for i in range(n-1,-1,-1):
    print(i)
    arr[i] = arr[i+1]
  arr[-1] = b
  return arr

print(rotate(a,len(a)))

# maxSubArray
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums1 = [5, 4, -1, 7, 8]
nums2 = [-2, 1]
nums3 = [-1]
nums4 = [-1, -2]
nums5 = [-2, -3, -1]
def maxSubArray(nums):
  sum1, sum2, i = 0, 0, 0
  j = -1
  dele = True
  # while i < len(nums) and -j < len(nums):
  while dele:
    dele = False

    # from left
    if len(nums) == 2:
      sumee = sum(nums)
      return sumee if nums[0] < sumee and nums[1] < sumee else nums[0] if nums[0] > nums[1] else nums[1]
    if len(nums) == 1:
      return sum(nums)

    sum1 += nums[i]
    if sum1 < 0:
      nums = nums[i + 1:]
      sum1 = 0
      i = -1
      dele = True
    i += 1

    # from right
    if len(nums) == 1:
      return sum(nums)

    sum2 += nums[j]

    if sum2 < 0:
      nums = nums[:j]
      sum2 = 0
      j = 1
      dele = True
    j -= 1
    print(nums, i, j)
  return sum(nums)

maxSubArray(nums5)