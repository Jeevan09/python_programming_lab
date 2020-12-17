#palindrome of a number or not using functions
n=int(input("Enter number:"))
def findpalin(n):
    x=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(x==rev):
        print(x,"number is a palindrome.")
    else:
        print(x,"number isn't a palindrome.")
findpalin(n);
