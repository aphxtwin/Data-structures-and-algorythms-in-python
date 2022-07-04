'''
Write a short Python function that counts the number of vowels in a given
character string
'''
def vowel_counter(string_of_data):
    vowel = ("a","e","i","o","u")
    count = 0
    for i in string_of_data:
        if i in vowel:
            count += 1
    print(count)
   
