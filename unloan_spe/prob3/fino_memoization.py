# def slow_add(a, b):
#     """
#     Pretend this is a slow operation (like complex calculation)
#     """
#     print(f"  🧮 Computing {a} + {b}...")  # Shows when we actually compute
#     return a + b

# def demonstrate_without_memoization():
#     """
#     Show how we recalculate the same thing multiple times
#     """
    
#     print("=== WITHOUT MEMOIZATION (Slow & Wasteful) ===")
#     print()
    
#     # Simulate a program that needs these calculations multiple times
#     print("Our program needs these calculations:")
    
#     result1 = slow_add(5, 3)
#     print(f"Result 1: {result1}")
    
#     result2 = slow_add(2, 7) 
#     print(f"Result 2: {result2}")
    
#     result3 = slow_add(5, 3)  # Same as result1 - but we recalculate!
#     print(f"Result 3: {result3}")
    
#     result4 = slow_add(2, 7)  # Same as result2 - but we recalculate!
#     print(f"Result 4: {result4}")
    
#     print()

# demonstrate_without_memoization()

# def demonstrate_with_memoization():
#     """
#     Show how memoization avoids recalculation
#     """
    
#     print("=== WITH MEMOIZATION (Fast & Smart) ===")
#     print()
    
#     # Our "memory" - a dictionary to store answers
#     memory = {}  # This is our "notes"
    
#     def memoized_add(a, b):
#         # Create a "key" to identify this problem
#         key = (a, b)
        
#         # Check if we already solved this
#         if key in memory:
#             print(f"  💡 Found in memory: {a} + {b} = {memory[key]}")
#             return memory[key]
        
#         # If not in memory, calculate it
#         print(f"  🧮 Computing {a} + {b}...")
#         result = a + b
        
#         # Store the answer in memory for next time
#         memory[key] = result
#         print(f"  📝 Storing in memory: ({a}, {b}) → {result}")
        
#         return result
    
#     result1 = memoized_add(5, 3)
#     print(f"Result 1: {result1}")
#     print()
    
#     result2 = memoized_add(2, 7)
#     print(f"Result 2: {result2}")
#     print()
    
#     result3 = memoized_add(5, 3)  # Same as result1 - but now we use memory!
#     print(f"Result 3: {result3}")
#     print()
    
#     result4 = memoized_add(2, 7)  # Same as result2 - but now we use memory!
#     print(f"Result 4: {result4}")
#     print()
# demonstrate_with_memoization()

def fibonacci_without_memoization(n):
    """
    Classic Fibonacci - VERY SLOW for large numbers
    F(n) = F(n-1) + F(n-2)
    """
    print(f"  Computing F({n})")  # Show each computation
    
    if n <= 1:
        return n
    
    return fibonacci_without_memoization(n - 1) + fibonacci_without_memoization(n - 2)

def demonstrate_fibonacci_problem():
    """
    Show why Fibonacci without memoization is terrible
    """
    
    print("=== FIBONACCI WITHOUT MEMOIZATION ===")
    print()
    print("Let's calculate F(5) and see how many computations happen:")
    print()
    
    result = fibonacci_without_memoization(5)
    print(f"\nF(5) = {result}")
    print()
    print("😱 Did you see how many times we computed F(3), F(2), F(1)?")
    print("😱 This gets exponentially worse for larger numbers!")
demonstrate_fibonacci_problem()