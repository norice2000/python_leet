import json

deployments = [
    '{"deployment_id": "d-123456789ab", "status": "Success"}',  # ← JSON string 1
    '{"deployment_id": "d-09876543cd", "status": "Fail"}'       # ← JSON string 2
]

def eval(deployments):
    success_count = 0
    fail_count = 0
    error_count = 0

    for deployment_json in deployments:

        try:
            # Convert JSON string to Python dictionary
            deployment = json.loads(deployment_json)
            
            if 'status' in deployment:
                status = deployment['status']
                # check for success
                if status == 'Success':
                    success_count += 1
                elif  status == 'Fail':
                    fail_count += 1
                else:
                    error_count += 1
            else:
                error_count += 1


            
        except Exception as e:
            return e
    return [success_count, fail_count, error_count]


print(eval(deployments))