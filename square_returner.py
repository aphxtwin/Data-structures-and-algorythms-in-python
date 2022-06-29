"""
r1.4
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
def n(k):

    listi= []
    while k > 0:
        k = k-1
        listi.append(k)

    result=0

    for i in listi:
        result= result+i**2
    print(result)
