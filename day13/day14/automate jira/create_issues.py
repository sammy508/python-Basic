# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://codesammy1000.atlassian.net//rest/api/3/issue"

api_token = "ATATT3xFfGF09stNjwCa16f7KUzHCqApTAq3xKAlou4LyC2I1YwNR89Hb3ruwiHgyuQjbl8r5UAYfEXESQ8y-Hd3S7f5EsB_p10DH5FeVaAaUSZjrstx9I6ZYZpD0JM93HqeQmc2axm7ezzgU2s7FEsFotjBNSShcBJwvSHYPCBS2mruhjBAb5w=C230DA75"


auth = HTTPBasicAuth("codesammy1000@gmail.com",api_token )

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
   
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    
    "issuetype": {
      "id": "10001"
    },
    "labels": [
      "bugfix",
      "blitz_test"
    ],
   
    "project": {
      "id": "10000"
    },
    
   
    "summary": "My first jira ticket",
    
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
