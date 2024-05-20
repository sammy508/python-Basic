# import os



import os
print(os.getenv("password"))
# Accessing an environment variable
db_host = os.getenv('DB_HOST', 'localhost')  # 'localhost' is the default value if DB_HOST is not set
print(f"Database Host: {db_host}")

# while run command   on powershell it execute but while running on cmnd prompt it shows KeyError

# # cmnd line for powershell:
# $env:password = "sammy"
# $env:Database Host = "127.0.0.1"