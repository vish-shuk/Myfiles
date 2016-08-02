# Declares whether the given string is a palindrome or not.
#Bitch ass stupid program doesn't recognise small and capital letters as same

word = raw_input("Enter a word: ")
word = word.lower()
if word[::-1] == word:
    print "%s is a palindrome." % word
else:
    print "Not a palindrome."
