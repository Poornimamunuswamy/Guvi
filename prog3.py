l=['a','e','i','o','u']
c=input("Enter a character ")
if(c.isalpha()):
    if c in l:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
