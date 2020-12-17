#count the n of occurance
def search(str,x):
    count=0
    for i in range(0,len(str)):
        if(x==str[i]):
            count+=1
    print("This character occured ",count," times")
print("\nEnter the string")
str=input()
print("Enter the character to be searched:")
x=input()
search(str,x)
