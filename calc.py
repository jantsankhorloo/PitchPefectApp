def gcd(a, c):
    """Returns the greatest common divisor of a and c by using Euclidean algorith"""
    while (c != 0):
        r = a%c
        a = c
        c = r
    return a

def calc(a, b, c):
    """a and c are numbers you want to do operations assigned to b"""
    while True:
        try:
            if b == '+':
                return a+c
            elif b == '-':
                return a-c
            elif b == '*':
                return a*c
            elif b == '/':
                return float(a)/c
            elif b == '**':
                return a**float(c)
            elif b == '%':
                return (float(c)/a)*100 #the sign % is used to shot what percent of a is c
            elif b == 'root':
                return a**(1.0/c) #takes a root to any given variable to input 'c', kind of reverse power
            elif b == 'gcd':
                return gcd(a, c)                                      
            else:
                return 'Invalid operation'
        except:
            return 'Please, check your inputs!'
 
        
        
