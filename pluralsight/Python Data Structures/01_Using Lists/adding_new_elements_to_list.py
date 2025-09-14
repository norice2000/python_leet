event_log = ["System start", "User login"]



print(event_log)
event_log.append("Hello")
print(event_log)

event_log.insert(1, "Happy Start")
print(event_log)

# Combinging 2 lists together
carbs = ["bread", "rice"]
protein = ["chicken", "beef"]

meal = carbs + protein # concatenation
meal.extend(["pork"]) #to extend, make sure to do it with a square bracket so it know it is a list!!

print(meal) #outputs ['bread', 'rice', 'chicken', 'beef', 'pork']