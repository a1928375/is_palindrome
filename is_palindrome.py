def is_palindrome(s):
    if s=="":
        return True
    else:
        i=0
        j=-1
        while i<(0.5*len(s)):
            while j>=-(0.5*len(s)):
                if s[i]==s[j]:
                    i=i+1
                    j=j-1
                else:
                    return False
        return True
 
 
print is_palindrome('')

print is_palindrome('abab')

print is_palindrome('abba')
