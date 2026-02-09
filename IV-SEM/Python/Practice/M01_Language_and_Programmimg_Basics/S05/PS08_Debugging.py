#Bug-->Error
#Finding anf Fixing of errors is called debugging.
'''
Types of Errors:
   1)Syntax Error,Ex:Missing of colon, Missing of Indentation
   2)Runtime Error,Ex: Division of any number with Zero
   3)Logical Error,Ex: missing of logics.
Debugging Techniques:
   1)Print()--> run the code line by line
   2)try - except 
   3)Using of pdb
'''
try:
    a = int(input("Enter a: "))
    print(10/a)
except ZeroDivisionError:
    print("Denominator should not be zero")
except ValueError:
    print("Invalid input, Please enter integer value only")
'''
pdb--> python debugger
    1)pause the flow of execution at any line
    2)inspect the variables value
    3) to run the code line by line
pdb commands:
    1)n-->to get output in next line
    2)p variable-->to get the value of that variable
    3)l -->list nearby code
    4)c --> continue the execution
    5)s --> start the fuction
    6)r --> to return from the function
    7)h -->help
    8)q -->quit the execution

'''
import pdb 
def add(a,b):
    pdb.set_trace()
    return a+b 
a= int(input("Enter a: "))
b= int(input("Enter b: "))
print("Sum:",add(a,b))
