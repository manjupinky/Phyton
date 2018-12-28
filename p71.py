w=raw_input()
rev_w = reversed(w)
if list(w) == list(rev_w):
   print("It is palindrome")
else:
   print("It is not palindrome")
