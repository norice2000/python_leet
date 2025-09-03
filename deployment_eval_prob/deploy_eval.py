import json

deployments = [
    '{"deployment_id": "d-123456789ab", "status": "Success"}',  # ← JSON string 1
    '{"deployment_id": "d-09876543cd", "status": "Fail"}'       # ← JSON string 2
]


class EvalDeployment:
    def __init__(self):
        self.error_msg = '[0, 0, 0]'

    def _validate(self, jsonlogs):
        success_counter = 0
        fail_counter = 0
        error_counter = 0

        for deployment in jsonlogs:
            try:
                deployment_dictionary = json.loads(deployment)
                status = deployment_dictionary['status']
                if status == 'Success':
                    success_counter += 1
                elif status == 'Fail':
                    fail_counter += 1
                else:
                    error_counter += 1
            except Exception as e:
                return self.error_msg
            
        return [success_counter, fail_counter, error_counter]


    def parse(self, jsonlogs):
        try:
            result = self._validate(jsonlogs)
            return result
        except Exception as e:
            return f"Error {e}"
        

instantiate = EvalDeployment()
result = instantiate.parse(deployments)
print(result)