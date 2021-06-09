def fibonacci(n):
    
    
    if n > 2:
        result = fibonacci(n-1) + fibonacci(n-2)
    else:
        result = 1
    return result
