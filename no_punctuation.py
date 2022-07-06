'''
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
'''
def without_punct(s):
    points = ("'",",","?",".",";",":")
    for i in s:
        if i in points:
            s = s.replace(i,"").lower()
    print(s) 
