def question2(a):
    maxLength = 1
 
    start = 0
    length = len(a)
 
    low = 0
    high = 0
 
    # One by one consider every character as center point of 
    # even and length palindromes
    for i in xrange(1, length):
        # Find the longest even length palindrome with center
    # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
 
        # Find the longest odd length palindrome with center 
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
 
    print "Longest palindrome substring is:",
    print a[start:start + maxLength]
   
 
 
# Driver program to test above functions
a = "forgeeksskeegfor"

print (question2(a))

 
