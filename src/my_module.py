OUTPUT_PATH = "/home/usr1/folder_name"

def armstrong_number3(num):
    '''
    Function to find whether the given number is Armstrong number or not.
    '''
    value = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        value = value +  digit ** 3
        temp = temp // 10
    
    # return the result
    if num == value:
        return True
    else:
        return False
    
def factorial(x):
    '''Calulate factorial '''
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# print(factorial(3))
if __name__ == "__main__":
    f3 = factorial(3)
    print("factorial of 3 is",f3)