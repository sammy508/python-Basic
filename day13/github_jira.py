from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def Jiraissue():
    url = "https://codesammy1000.atlassian.net/rest/api/3/issue"

    # Fetch the API token from an environment variable or a configuration file for security
    api_token = os.getenv('JIRA_API_TOKEN', 'your_api_token_here')

    auth = HTTPBasicAuth("codesammy1000@gmail.com", api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get JSON payload from the POST request
    payload = request.json

    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
