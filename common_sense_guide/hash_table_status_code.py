
# instead of this
def status_code_meaning(number):
    if number == 200:
        return "OK"
    elif number == 301:
        return "Moved"
    elif number == 404:
        return "Not Found"
    


# Using hash table
status_codes = {
    200: 'OK',
    301: 'Moved',
    404: 'Not Found'
    }

def status_code_hash(number: dict) -> dict:
    
    return status_codes.get(number)

result = status_code_hash(200)
print(result)