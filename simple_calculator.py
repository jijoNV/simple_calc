
def add(num1,num2):
    addition = num1+num2
    print("Sum =",addition)

def sub(num1,num2):
    subt = num1-num2
    print("Difference =",subt)

def mul(num1,num2):
    mult = num1*num2
    print("Product =",mult)

def div(num1,num2):
    divs = num1/num2
    print("Quotient =",divs)

print('''1. Addition\n'
      2. Subtraction\n
      3. Multiplication\n
      4. Division''')
choice = int(input("Enter your choice (1,2,3,4):"))
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

if(choice==1):
    add(num1,num2)
elif(choice==2):
    sub(num1,num2)
elif(choice==3):
    mul(num1,num2)
elif(choice==4):
    div(num1,num2)
else:
    print("Invalid choice")





