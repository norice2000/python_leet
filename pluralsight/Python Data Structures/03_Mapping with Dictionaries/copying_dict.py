# dictionary re-assignment in variable is just an alias

original = {"theme": "dark"}

shallow_copy = original.copy()
# You can also use dict()
# shallow_copy = dict(original)

shallow_copy["theme"] = "light"

#deep copy
import copy

deep_copy = copy.deepcopy(original)
deep_copy["theme"] = "purple"

print(f"original: {original}")
print(f"shallow_copy: {shallow_copy}")
print(f"deep_copy: {deep_copy}")

# original: {'theme': 'dark'}
# shallow_copy: {'theme': 'light'}
# deep_copy: {'theme': 'purple'}