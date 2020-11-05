x = int(input ("Please enter the Total Number of list Elements:"))
a =[]
for z in range(x):
    z +=1
    number = int( input("Please enter the Value of {0} Elemens:" .format(z)))
    if ( x % 2 != 0):
        a.append(x)
print(a)
