import requests
'''

todo = {
    "userId": 1,
    "title": "Buy milk",
    "completed": false
}
# python dict
todo = {"userId": 1, "title": "Buy milk", "completed": False}

requests.post(url,json=todo) # python dict is sent here

When you do this, requests.post() sets the HTTP header Content-Type of the request to application/json. 
It also converts todo into a JSON string, which it adds to the request’s body.

If you don’t use the JSON keyword argument to deliver JSON data, you’ll have to manually define the 
Content-Type and serialize the JSON. Here’s a replacement for the prior code:

>>> import requests
>>> import json
>>> api_url = "https://jsonplaceholder.typicode.com/todos"
>>> todo = {"userId": 1, "title": "Buy milk", "completed": False}
>>> headers =  {"Content-Type":"application/json"}
>>> response = requests.post(api_url, data=json.dumps(todo), headers=headers)
>>> response.json()
{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

>>> response.status_code
201 
     
 

'''