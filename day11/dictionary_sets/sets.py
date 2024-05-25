emp_details = [
    {
        "name":"sammy",
        "gender":"male",
        "address":"butwal"
    },
    {
        "name":"sangam",
        "gender":"male",
        "address":"pkr"
    },
    {
        "name":"suman",
        "gender":"male",
        "address":"butwal"
    }
]
print(emp_details[0]["name"])
print("here we will print only name of the employee using for loop")

for i in range (len(emp_details)):
 print(emp_details[i]["name"])