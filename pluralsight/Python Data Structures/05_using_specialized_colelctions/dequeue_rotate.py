# we can use rotate to manouve the data
from collections import deque

schedule = deque(['champ', 'lucky', 'lulu'])

#simulate 3 weeks rotation
for week in range(1, 4):
    print(f"Week: {week}, schedule: {list(schedule)}")
    schedule.rotate()

# Week: 1, schedule: ['champ', 'lucky', 'lulu']
# Week: 2, schedule: ['lulu', 'champ', 'lucky']
# Week: 3, schedule: ['lucky', 'lulu', 'champ']