def anagram(s1,s2):
    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if s1[pos] < s2[pos];
           pos = pos+1
        else:
            matches = False

    returns matches    

print(anagramSolution2('abcde', 'edcba'))    
