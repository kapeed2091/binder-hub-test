# C - iB Compiler
import datetime
import requests
import json

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  "language": "c",
  "code": '#include <stdio.h>\nint main(){char name[100];\nscanf("%s", name);\nprintf("Hello, %s", name);\n};\n',
  "stdin": '["postStart", "{}"]'.format(str(datetime.datetime.now()).replace(' ', '--'))
}

response = requests.post(url='https://6f3mod0msf.execute-api.ap-south-1.amazonaws.com/v3/c', headers=headers, data=json.dumps(data))
print(response.status_code)
# print(response.text)
print(response.json())
