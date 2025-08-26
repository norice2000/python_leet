numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# # bad practice
# for number in numbers:
#     print(f"{number} {letters[0]}")
#     print(f"{number} {letters[1]}")
#     print(f"{number} {letters[2]}")

# # preferred nested
# print("nested")
# for number in numbers:
#     for letter in letters:
#         print(f"{number} {letter}")


# trialing out parralising
from joblib import Parallel, delayed
import time

my_list = [1,2,3,4]
my_squares = []

def slow_square(i):
    time.sleep(1)
    squared = i * i
    return squared

my_squares = Parallel(n_jobs=-1)(delayed(slow_square)(i) for i in my_list)

print(my_squares)