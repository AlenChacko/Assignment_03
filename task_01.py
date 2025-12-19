number=int(input("Enter a number: "))

def factorial(num):
    """
    Calculating the factorial of given number using recursion
    :param num: An integer whose factorial is to be calculated
    :return: The factorial of the given number
    """
    if num ==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)

result=factorial(number)
print(f"Factorial of {number} is : {result}")