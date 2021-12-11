a=int(input('Enter First Number'))
b=int(input('Enter Second Number'))

#adding addion 
def addition(x,y):
    return x+y

print(a,"+",b,"=", addion(a,b))

#adding substraction
def subs(x,y):
    return x-y

print(a,"-",b,"=", subs(a,b))

#adding multiplication

def mul(x,y):
    return x*y

print("Multiply is ", mul(a,b))

#adding division

def div(x,y):
    return x/y

print("Division is ", div(a,b))

