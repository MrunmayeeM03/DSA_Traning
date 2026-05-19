def stock_span(price):
    n = len(price)
    span = [1] * n  
    stack = []     

    for i in range(n):
       
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()
        
       
        span[i] = i + 1 if not stack else i - stack[-1]
        
        stack.append(i)
    
    return span


price = [100, 80, 60, 70, 60, 75, 85]
result = stock_span(price)
print("Price: ", price)
print("Span:  ", result)