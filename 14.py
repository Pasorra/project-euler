def collatz(n, memo):
    if n in memo.keys():
        return memo[n]
    
    if n % 2 == 0:
        val = collatz(n // 2, memo)
        memo[n] = val + 1
        return val + 1
    
    else:
        val = collatz((3 * n) + 1, memo)
        memo[n] = val + 1
        return val +     1
        

longest_terms = 0
longest_i = 0
memo = {1:1}
for i in range(1, 1_000_000):
    terms = collatz(i, memo)
    if terms > longest_terms:
        longest_terms = terms
        longest_i = i
        
print(longest_i)