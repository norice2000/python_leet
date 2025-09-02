#Real Interview Scenario:
# When an interviewer asks "Process 1 million server logs to find all errors," you now know:

# Use an array to store logs
# Loop through once (O(n))
# Filter errors into a new array
# Consider batching for better performance

# class InspectorLogs:
#     def __init__(self):
#         self.error_message = "invalid"
    
#     def _find_error(self, logs):
#         error_logs = []
#         for log in logs:
#             if 'ERROR' in log:
#                 error_logs.append(log)
#         return error_logs
    
#     def parse(self, logs):
#         try:
#             error_result = self._find_error(logs)
#         except Exception as e:
#             return self.error_message
#         return error_result

# server_logs = [ "2024-01-15 INFO: User logged in", "2024-01-15 ERROR: Database connection failed", "2024-01-15 INFO: Request processed", "2024-01-15 ERROR: Timeout occurred" ]
# inspector = InspectorLogs()
# result = inspector.parse(server_logs)
# print(str(result))

# Imagine you're monitoring 1000s of server logs per minute. You need to:

#     Store them in order
#     Find errors quickly
#     Process them in batches

server_logs = [ "2024-01-15 INFO: User logged in", "2024-01-15 ERROR: Database connection failed", "2024-01-15 INFO: Request processed", "2024-01-15 ERROR: Timeout occurred" ]


# Goal look for error and append the results of the error
class InspectLogs:
    def __init__(self):
        self.error_message = "Invalid"

    def _error_log_(self, logs: list):
        # create empty list error counter
        # for loop to iterate through the list
        # if condition for the word ERROR
        # TRUE append error_counter to meet 0(1)
        # return error_counter
        error_counter = []
        for log in logs:
            if 'ERROR' in log:
                error_counter.append(log)
        return error_counter
    
    def parse(self, logs:list):
        try:
            check_erorr = self._error_log_(logs)
        except:
            return self.error_message
        return check_erorr


result = InspectLogs().parse(logs=server_logs)
print(str(result))