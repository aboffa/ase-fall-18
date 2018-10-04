#calculator.py 

def sum(m,n):
    result=m
    if n > 0:
        for i in range(n):
            result+=1
    else:
        for i in range(abs(n)):
            result-=1
    return result

def divide(m,n):
    if n==0 :
	    raise ZeroDivisionError()
		
    result=0
    negativeResult=False
    if n < 0:
        n*=-1
        negativeResult = not negativeResult
    if m < 0: 
        m*=-1
        negativeResult = not negativeResult
    while((m-n)>=0):
        m-=n
        result+=1
    result = -result if negativeResult else result
    return result

