



                


# def server_update(file_path, key, value):
#     with open(file_path, "r") as file:
#         lines = file.readlines()

#     with open(file_path, "w") as file:
#         for line in lines:
#             if key in line:
#                 file.write(f"{key}={value}\n")
#             else:
#                 file.write(line)

# # Call the function with value converted to string
# server_update("server.conf", "MAX_CONNECTIONS", 1000)

# def server_update(path, key, value):
#     with open(path, "r") as file:
#         lines = file.readlines()

#     with open(path, "w") as file:

#          for line in lines:

#             if key in line:
#                file.write(f"{key}={value} \n")
#             else:
#                file.write(line)
# filepath = "D:/pythonfordev/python-for-devops/day12/serverdetail.confi"
# server_update(filepath,"MAX_CONNECTIONS",1000)  

# def server_update(path, key, value):
#     value = str(value)  # Ensure the value is a string

#     try:
#         # Open the file for reading
#         with open(path, "r") as file:
#             lines = file.readlines()
        
#         # Open the file for writing
#         with open(path, "w") as file:
#             for line in lines:
#                 if line.startswith(key + "="):
#                     file.write(f"{key}={value}\n")
#                 else:
#                     file.write(line)
#     except FileNotFoundError:
#         print(f"File not found: {path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# filepath = "D:/pythonfordev/python-for-devops/day12/serverdetail.confi"
# server_update(filepath, "MAX_CONNECTIONS", 1000)
