# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

# your jira url/ esc2 instance url
url = "https://code.atlassian.net//rest/api/3/issue"

api_token = " your api token"

auth = HTTPBasicAuth("your@1gmail.com",api_token )

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
