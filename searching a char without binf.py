#searching a character without built in functions
main = "welcome to the world of python"
sub = input("enter the character to be found:")
count = 0
for i in range (0,len(main)):
   match = True
   if sub[0]==main[i]:
     j=0
     for j in range(0,len(sub)):
         if sub[j]!=main[i+j]:
             match = False
             print("Not found")
             break
         else:
             count=count+1
             if match == True and count == len(sub):
                 print("found character")
                 print("index no:",i)
