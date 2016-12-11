# Question 1
    
def question1(s, t):
    # Return True if t is empty
    if t == '':
        return True
    # Return False if s and t are not strings
    if type(s) != str or type(t) != str:
        return False

    # Remove the spaces and make letters lowercase.
    s = s.replace(' ', '').lower()
    t = t.replace(' ', '').lower()

    # Return False if s is empty or length of s is shorter than length of t
    if len(s) < len(t) or len(s)==0:
        return False

    tdict = {}
    # Put the count and letters of t into tdict
    for i in range(len(t)):
        tdict[t[i]] = t.count(t[i])
    # Create a empty dictionary(s_dict) for each substring in s of len(t)
    for i in range(len(s)-len(t)+1):
        sub_str_s = s[i:i+len(t)]
        s_dict = {}
        # Put the count and letters of substring of s into s_dict
        for j in range(len(t)):
            s_dict[sub_str_s[j]] = sub_str_s.count(sub_str_s[j])
            
        # Return True if s_dict and tdict are equal
        if s_dict == tdict:
            return True            
    return False


print "Question 1"
# False
print question1('     ','is')
# False
print question1(123, 1435)
# True
print question1('My Name .Is Eunbi Go','mies.')
# False
print question1('udacity', 'aDyQ')

