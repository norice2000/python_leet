
# Example: "Parse this server log and count error types"
logs = [
    {"server": "web-01", "status": "healthy"},
    {"server": "web-02", "status": "unhealthy"}, 
    {"server": "db-01", "status": "healthy"},
    {"server": "db-02", "status": "healthy"}
]

# Expected Output: {"healthy": 3, "unhealthy": 1}


def main():
    count_status(logs)

def count_status(health_checks):
    # create empty dict
    status_count = {}
    #parse log
    print(health_checks)
    for check in health_checks:
        status = check["status"] #printing the result after status:
    # for loop through the log
        if status in status_count:
            status_count[status] += 1 # if healthy detected, increment healthy
        else:
            status_count[status] = 1 #if already counted, leave it as one

    return status_count
    # if condition ERROR: Connection failed match, counter_fail increment
    # elif ERROR Memory limit exceeded
    # return print

if __name__ == "__main__":
    main()