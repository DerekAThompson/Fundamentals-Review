""""
Write a function that determines if a word is a palindrome or not
Clarify assumptions
x is a string of lenth n where 1 < n < 100
"""

def palindrome(x):
    if x == x[::-1]:
        return True
    return False


"""
Given a string, find the longest substring that is a palindrome
Assumptions: String is always alphabetic characters, 0 < len(String), 
a single character can be classified as a palindrome, lower case letters only
"""

def longestSubPalindrome(yourString):
    maxCount = 0
    longestPal = []
    for lefty in range(len(yourString)):
        if maxCount >= len(yourString[lefty:]):
            break
        for righty in range(lefty, len(yourString)):
            subList = yourString[lefty:righty + 1]
            if palindrome(subList):
                count = len(subList)
                if count > maxCount:
                    maxCount = count
                    longestPal = subList
    return longestPal, maxCount



def checkTwo(yourString):
    count = 0
    maxCount = 0
    

    for i in range(len(yourString)):
        # case 1
        if palindrome(yourString[i :i + 2]):
            recursePal(yourString, i, i + 1)    


        # case 2
        if palindrome(yourString[i - 1:i + 2]):
            recursePal(yourString, i - 1, i + 2)


def recursePal(yourString, left, right):
    if palindrome(yourString[left - 1:right + 2]):
        recursePal(yourString, left - 1, right + 2)
    else:
        return len(yourString[left - 1:right + 2]) - 2

    




print(longestSubPalindrome('joey'), 'Expect: J, 1')
print(longestSubPalindrome('kayak'), 'Expect: kayak, 5')
print(longestSubPalindrome('goofs'), 'Expect: oo, 2')
print(longestSubPalindrome('d'), 'Expect: Q, 1')
print(longestSubPalindrome('kraccooccarxyz'), 'Expect: raccooccar, 10')
