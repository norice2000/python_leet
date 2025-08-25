# numerator = float(input("Etner numerator: ")) 
#if i intentionally put a letter itll give me ValueError

# phoodie@fedora:~/Documents/git/python_leet$ /sbin/python /home/phoodie/Documents/git/python_leet/try_except.py
# Etner numerator: asdf
# Traceback (most recent call last):
#   File "/home/phoodie/Documents/git/python_leet/try_except.py", line 1, in <module>
#     numerator = float(input("Etner numerator: ")) #if i intentionally put a letter itll give me ValueError
# ValueError: could not convert string to float: 'asdf'


# denominator = float(input("Enter denominator: ")) #if i intentionally put letter itll give me ZeroDivisionError

# after executing these lines individually we get an idea what our except error msg to be in our try block
# if unsure,use except Exception as e
try:
    numerator = float(input("Etner numerator: "))
    denominator = float(input("Enter denominator: "))
    quotient = numerator / denominator
    print(f"The quotient is {quotient}")
except ValueError:
    print("enter valid number")

except Exception as e:
    print(f"error: {e}")