

Number = int(input("Enter any number"))
Sum = 0
for i in range(1,Number):
    if(Number % i == 0):
        Sum = Sum +1
if(Sum == Number):
    print("%d Is a perfect Number" %Number)
else:
    print("%d Is not a perfect Number" %Number)



