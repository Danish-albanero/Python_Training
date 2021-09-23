#1-Anagram check

def anagram(s, s1):
    if sorted(s) == sorted(s1):
        print("anagram")
    else:
        print("Not an anagram")
s="cat"
s1="tac"

anagram(s,s1)
