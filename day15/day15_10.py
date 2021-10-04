#10-Count all lower case, upper case, digits,
#and special symbols from a given string
def countChar(S):
  charC = 0
  digit = 0
  symbol = 0
  for char in S:
    if char.islower() or char.isupper():
      charC+=1
    elif char.isnumeric():
      digit+=1
    else:
      symbol+=1
      
  print("Chars = ", charC, "Digits = ", digit, "Symbol = ", symbol)
      
S= "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")

countChar(S)
