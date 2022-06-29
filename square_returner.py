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

"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
def n(k):
    if k > 0:
        listi= []
        while k > 0:
            k = k-1
            if k%2 != 0:
                listi.append(k)
        
        result=0
    
        for i in listi:
            result= result+ i**2
        print(result)
