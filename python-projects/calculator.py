# This is the calculator program

try:
    def sum(num1,num2):
        return num1+num2
    def subtract(num1,num2):
        return num1-num2
    def multiply(num1,num2):
        return num1*num2
    def division(num1,num2):
        return num1/num2

    def sum2(result,num3):
        return result+num3
    def subtract2(result,num3):
        return result-num3
    def multiply2(result,num3):
        return result*num3
    def division2(result,num3):
        return result/num3

    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    user_choice=input("Which operation you want to perform?\n+,-,/,*\n")
    if user_choice=="+":
        result=sum(num1,num2)
        print(f"The addition of two number is {result}")
        user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no")
        while(user_second_choice=="yes"):
            num3 = int(input("Enter the second number:"))
            user_choice = input("Which operation you want to perform?\n+,-,/,*\n")
            if user_choice=="+":
                result=sum2(result,num3)
                print(f"The addition of two number is {result}")
            elif user_choice=="-":
                result=subtract2(result,num3)
                print(f"The subtraction of two number is {result}")
            elif user_choice=="*":
                result=multiply2(result,num3)
                print(f"The multiplication of two number is {result}")
            elif user_choice=="/":
                result=division2(result,num3)
                print(f"The divison of two number is {result}")
            user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no:")
    elif user_choice == "-":
        result = subtract(num1, num2)
        print(f"The subtraction of two number is {result}")
        user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no")
        while (user_second_choice == "yes"):
            num3 = int(input("Enter the second number:"))
            user_choice = input("Which operation you want to perform?\n+,-,/,*\n")
            if user_choice == "+":
                result = sum2(result, num3)
                print(f"The addition of two number is {result}")
            elif user_choice == "-":
                result = subtract2(result, num3)
                print(f"The subtraction of two number is {result}")
            elif user_choice == "*":
                result = multiply2(result, num3)
                print(f"The multiplication of two number is {result}")
            elif user_choice == "/":
                result = division2(result, num3)
                print(f"The divison of two number is {result}")
            user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no:")
    elif user_choice == "*":
        result = multiply(num1, num2)
        print(f"The multiplication of two number is {result}")
        user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no")
        while (user_second_choice == "yes"):
            num3 = int(input("Enter the second number:"))
            user_choice = input("Which operation you want to perform?\n+,-,/,*\n")
            if user_choice == "+":
                result = sum2(result, num3)
                print(f"The addition of two number is {result}")
            elif user_choice == "-":
                result = subtract2(result, num3)
                print(f"The subtraction of two number is {result}")
            elif user_choice == "*":
                result = multiply2(result, num3)
                print(f"The multiplication of two number is {result}")
            elif user_choice == "/":
                result = division2(result, num3)
                print(f"The divison of two number is {result}")
            user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no:")
    elif user_choice == "/":
        result = division(num1, num2)
        print(f"The divison of two number is {result}")
        user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no")
        while (user_second_choice == "yes"):
            num3 = int(input("Enter the second number:"))
            user_choice = input("Which operation you want to perform?\n+,-,/,*\n")
            if user_choice == "+":
                result = sum2(result, num3)
                print(f"The addition of two number is {result}")
            elif user_choice == "-":
                result = subtract2(result, num3)
                print(f"The subtraction of two number is {result}")
            elif user_choice == "*":
                result = multiply2(result, num3)
                print(f"The multiplication of two number is {result}")
            elif user_choice == "/":
                result = division2(result, num3)
                print(f"The divison of two number is {result}")
            user_second_choice = input("Do you want perform further operations on the resulted number?\nyes or no:")
except Exception as e:
    print(e)

