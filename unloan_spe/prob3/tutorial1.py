# one branch
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

#two branch
def two_factorial(n):
    if n <= 1:
        return n
    
    return two_factorial(n - 1) + two_factorial(n - 2)


class Solution:
    def memo_fib(self, n: int) -> int:
        # cache
        memo = {
            0:0,
            1:1
            }
        
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
            
        return f(n)
    
fib = Solution()
print(fib.memo_fib(2))
# print(two_factorial(2))