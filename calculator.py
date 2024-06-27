def addition(a,b):
    return a+b
def substaction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
n1=int(input("Enter 1st no.:"))
n2=int(input("Enter 2nd no.:"))
print("select operation:\n 1.Addition\n 2.Substaction\n 3.Multiplication\n 4.Division\n")



while True:
    choice=int(input("Enter choice 1/2/3/4:"))
    if choice==1:
        print(addition(n1,n2))
    elif choice==2:
        print(substaction(n1,n2))
    elif choice==3:
        print(multilication(n1,n2))
    elif choice==4:
        print(division(n1,n2))
    else:
        print("invilid input")
    break
