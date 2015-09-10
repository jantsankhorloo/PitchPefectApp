def pNumCheck(n):
    """Returns prime if the given number is a prime number and non-prime otherwise""" 
    if (n != 0) or (type(n) == "<type 'int'>"): #the input got to be an integer
        i = 2 #the first number is being counted from the number 2
        while i < n:
            if n == 2:
                return 'prime'
            elif n == 1:
                return 'non-prime'
            elif n % i == 0:
                return 'non-prime'
            i = i + 1
        else:
            return 'prime'
     
        
def NthPrime(n):
    """Returns n th prime number"""
    i=1
    while i<n:
        if pNumCheck(i) == 'prime':
            print str(i)
        i=i+1
