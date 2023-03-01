import requests

res = requests.get("http://127.0.0.1:5550/api/flask_test")
print(res.json())


re = requests.put("http://127.0.0.1:5550/api/flask_test")
print(type(re.json()))

