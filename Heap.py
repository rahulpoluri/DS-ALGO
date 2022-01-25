# creating min heap
a = [5,4,3,2,1,3,21]
print(a)

def heapify(a):
  swap = True
  while swap:
    swap = False
    for i in range(len(a)-1, -1, -1):
      child = i
      parent = i//2
      if a[parent]> a[child]:
        a[parent],a[child] = a[child],a[parent]
        swap = True
  return a

print(heapify(a))

def getmin(a):
  return a[0]

print(getmin(a))

def extractmin(a):
  b = a[0]
  a = a[1:]
  a = heapify(a)
  return a
a = extractmin(a)
print(a)
a = extractmin(a)
print(a)


def insert(ele):
  a.append(ele)
  return heapify(a)

a = insert(3.8)
print(a)