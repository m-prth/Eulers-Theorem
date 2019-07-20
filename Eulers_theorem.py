def f(x,y):
    return (y-((2*x)/y))
print("Enter the values of x0,y0,h and xn:")
x0 = float(input("x0:",))
y0 = float(input("y0:",))
h = float(input("h:"))
xn = float(input("xn:"))
n  = int((xn-x0)/h)
for i in range( 0,n+1):
    yn = y0+(h*f(x0,y0))
    x0 = x0+h
    y0 = yn
    print("Ans is:",yn,"The value of i is",i)
