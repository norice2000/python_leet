# Unpacking Dictionaries with the `**` Operator
def greet(greeting, name):
    print(f"{greeting}, {name}!")

# standard approachj
greet("Hello", "champ")

#kwargs = key word argument, make sure the key matches the function
kwargs = {
    "greeting": "hi",
    "name": "champ"
}

greet(**kwargs) #remebmer to use two **

## Can also Pack keyword Arguments with the `**` Operator
def log_event(event_type, **metadata):
    print(f"Event: {event_type}")
    print(f"Details: {metadata}")

log_event("login", user="anon", location="/dev/null") # see how we can add in more of our argument
# output
# Event: login
# Details: {'user': 'anon', 'location': '/dev/null'}

# this example is good for parsing HTML Tags
