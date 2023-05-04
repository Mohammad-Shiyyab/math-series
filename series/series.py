def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
 
# Driver Program
 
print(fibonacci(9))



def lucas(n) :
    a = 2
    b = 1
    if (n == 0) :
        return a
    for i in range(2, n + 1) :
        z =a + b
        a = b
        b = z
     
    return b
     
  
# Driver Code
# n = 9
print(lucas(7))
  


def sum_series (n,a=0,b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b   
     
  
# Driver Code

print(sum_series(6,6,8))         


 