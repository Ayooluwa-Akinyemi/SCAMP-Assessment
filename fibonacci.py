#this function helps return the fibonacci value for any given number

def fibonacci (f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)

#this function prints the fibonacci sequence for any given number
#it does this by looping through each values of a given number and returning the fibonacci value for each 

def fibonacci_sequence(f):
    for i in range (f + 1):
        print (fibonacci(i))
