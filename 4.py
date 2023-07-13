from utils import is_palindrome

result = 0
for y in range(999, 99, -1):
    for x in range(999, 99 , -1):
        product = x * y
        if product < result: break
        if not is_palindrome(product): continue 
        result = max(result, product)
        

print(result)
            
