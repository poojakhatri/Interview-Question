#Reverse a String

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = input("Enter any String: ") 
print(s)
print(reverse(s))