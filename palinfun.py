#to find paindrome of a string in functions
s=input("Enter a string :")
def findpalin(str):  
    for i in range(0, int(len(str)/2)):  
        if str[i] != str[len(str)-i-1]:
            print(s,"is not a palindrome")
    print(s,"is a palindrome.")
findpalin(s);
