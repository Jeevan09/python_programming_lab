def sqre(x):
    return(x**2)
squares=[]
squares=list(filter(sqre,range(1,11)))
print("list of squares in the range -10=:",squares)
sum=0
for i in squares:
    sum+=i
print("sum of squares in the range 1-10=",sum)
