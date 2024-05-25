import requests 


# ?repo/{owner}/{repo}/pulls
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(f"{response}")

complete_detail = response.json()

for i in range (len(complete_detail)):
    print(complete_detail[i]["user"]["login"] )