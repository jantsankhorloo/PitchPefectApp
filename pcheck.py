def ptest(a):
    while a > 1:
        if a == 2 or a == 3 or a == 5:
            return True
            if a == 4: return False
            while a > 5:
                if a%2 != 0 and a%3 != 0 and a%5 != 0:
                    return True
        else: return False 
