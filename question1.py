def question1(s,t):
    s = list(s)
    t = list(t)

    s.sort()
    t.sort()

    pos = 0
    matches = True

    while pos < len(s) and matches:
        if s[pos] == t[pos]:
           pos = pos+1
        else:
            matches = False

    return matches    

print(question1('udacity', 'cityuda'))
print(question1('udacity','t'))
print(question1('palindrome','romepalind'))
