
#The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two
def  fibonacci(n):
    if type(n) != int:
        return ("only integer is allowed")
    if n < 0:
        return ("sorry the range of number is from 0 to ∞")
    if n<=1:
      return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def list_fibonacci(numbers: list) -> list: 
    return [fibonacci(num) for num in numbers]


# The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.

def  lucas(n):
    if type(n) != int:
        return ("only integer is allowed")
    if n < 0:
        return ("sorry the range of number is from 0 to ∞")
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def list_lucas(numbers: list) -> list: 
    return [lucas(num) for num in numbers]



def sum_series(n , first , second):
    if type(n) != int:
        return ("Invalid Input")
    elif n < 0:
        return ("Invalid Negative Value")
    elif n == 0:
       return first
    elif n == 1:
       return second
    else:
       return (sum_series(n-1 , first , second ) + sum_series(n-2 , first , second ))
def list_sum_series(numbers: list , first : int , second : int) -> list: 
    return [sum_series(num , first , second ) for num in numbers]