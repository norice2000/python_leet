# cannot add
# Remove() elements

planets = {"earth", "mars", "screwdriver"}

planets.discard("earth")
print(planets)


# can remove with pop, do note since sets are unordered it will remove random one
# good for when you just need an arbitary element

# Clearing set with `clear()`

#updae elements with `update()`
planets.update(["dog", "lulu"]) # remember to add it as a list, or else it will add be each letter
print(planets)