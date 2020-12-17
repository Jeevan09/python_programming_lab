#write a python program to check given number is odd or even
num = int(input("Enter a number: "))
x = num % 2
if x > 0:
    print(num,"is an odd number.")
else:
    print(num,"is an even number.")
