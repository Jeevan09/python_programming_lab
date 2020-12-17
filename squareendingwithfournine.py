#squares of number from 1 to 100 end with 4 or 9
for i in range(1,100):
    x=i*i
    if(x%10==4):
        print(x,"is the square ending with '4'")
    elif(x%10==9):
        print(x,"is the square ending with '9'")
        
