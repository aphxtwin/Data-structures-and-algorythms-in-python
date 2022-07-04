'''
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
'''

def func(a,b):
  '''
  while loop aproach
  '''
    if len(a) == len(b):
        count = 0
        c = []
        while count < len(a):
            listac = a[count]*b[count]
            c.append(listac)
            count += 1
        print(c)
            
def funca(a,b):
  '''
  for loop aproach
  '''
    if len(a) == len(b):
        count = 0
        c = []
        for i in range(len(a)):
            listaco = a[count]*b[count]
            count += 1
            c.append(listaco)
        print(c) 
