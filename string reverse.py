#reverse of a string
def reverse(str): 
  s = "" 
  for i in str: 
    s = i + s
  return s
print("\nEnter the string")
str=input()
print("The original string  is : ",end="") 
print(str) 
print("The reversed string(using loops) is : ",end="") 
print(reverse(str))
