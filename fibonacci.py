# Recursive Approach

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
    
# Test case #1
print(fib_rec(6))

# Test case #2
#print(fib_rec(100))

# Top-Down Approach of DP

def fib_dp1(n):
    # Initialized memo as list of length n, fill with None
    # using to stoe the results of subproblems
    memo = [None] * (n + 1)

    def fib(n):
        if n < 2:
            memo[n] = n
        if memo[n] is None: 
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    
    return fib(n)

# Test case #3
print(fib_dp1(6))

# Test case #4
print(fib_dp1(100))

# Bottom-Up Approach of DP

def fib_dp2(n):
    dp = [0 ,1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


# Test case #5
print(fib_dp2(6))

# Test case #6
print(fib_dp2(100))

# Challenge 1 Space Optimized Approach
def fib_optimized(n):
    if n < 2:
        return n
    # a and b are the two variables to store the last two values
    a, b = 0, 1
    # loop through the range of 2 to n + 1
    for _ in range(2, n + 1):
        # swap the values of a and b, and add them together store the result in b
        # reducing the space complexity to O(1)
        a, b = b, a + b
    return b

# Test case #7
print(fib_optimized(6))

# Test case #8
print(fib_optimized(100))
