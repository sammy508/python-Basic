# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://codesammy1000.atlassian.net/rest/api/3/project"


api_token = "ATATT3xFfGF09stNjwCa16f7KUzHCqApTAq3xKAlou4LyC2I1YwNR89Hb3ruwiHgyuQjbl8r5UAYfEXESQ8y-Hd3S7f5EsB_p10DH5FeVaAaUSZjrstx9I6ZYZpD0JM93HqeQmc2axm7ezzgU2s7FEsFotjBNSShcBJwvSHYPCBS2mruhjBAb5w=C230DA75"

auth = HTTPBasicAuth("codesammy1000@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


output = json.loads(response.text) # when we have to parse json we use loads to convert json to dictionary to perfom operation

name = output[0]["name"]

print(name)  # it prints the projects name from jira

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))






