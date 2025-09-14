from collections import deque

#create waitlist
waitlist = deque()

# Append new elements
def arrive(name, vip=False):
    if vip:
        waitlist.appendleft(name)
        print(f"VIP customer {name} added to the front")
    else:
        waitlist.append(name)
        print(f"Regular customer {name} back of the line")
    print(waitlist)

arrive("lucky")
arrive("katie")
arrive("champ", vip=True)

# Regular customer lucky back of the line
# deque(['lucky'])
# Regular customer katie back of the line
# deque(['lucky', 'katie'])
# VIP customer champ added to the front
# deque(['champ', 'lucky', 'katie'])

def seat_customer():
    if waitlist:
        name = waitlist.popleft()
        print(f"customer {name} been seated")
    else:
        print(f"wait list empty")
    print(waitlist)

seat_customer()
# customer champ been seated
# deque(['lucky', 'katie'])