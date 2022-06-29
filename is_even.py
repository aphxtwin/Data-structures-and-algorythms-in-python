"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):
    num = str(k)[::-1]
    listi=["0","2","4","6","8"]
    if num[0] in listi:
        print(True)
    else:
        print(False) 
