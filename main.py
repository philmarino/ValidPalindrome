def isPalindrome(s):
    #strip all non-alpha
    temp = ''
    for letter in s:
        if letter.isalpha():
            temp += letter.lower()
    
    #reversed = temp[::-1]
    return temp == temp[::-1]


#Example 1:
#Input: 
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

#Example 2:
#Input: 
s = "race a car"
print(isPalindrome(s))
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: 
s = " "
print(isPalindrome(s))
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
