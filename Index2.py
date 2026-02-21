try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num1 // num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by Zero is error!!")

except SyntaxError :
    print("Comma is missing. Nuber should be seperated by a comma like this 1, 2")

except :
    print("Wrong Input") 

else :
    print("No exceptions")

finally :
    print("This will excecute no matter what")
