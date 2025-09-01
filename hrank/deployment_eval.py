import json

# python_dict = {"dog": "champ", "status": "success"}
# json_string = json.dumps(python_dict)
# print(json_string) #outputs '{"dog": "champ", "status": "success"}'

json_string = '{"deployment_id": "d-123", "status": "Success"}' #need the quotes at the end to escape the curly { }
conv_python_dict = json.loads(json_string)
print(conv_python_dict) # outputs {'deployment_id': 'd-123', 'status': 'Success'}