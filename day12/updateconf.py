

# here i got an error ther's no fault on code and method but it always says it can't find my file maybe it was on d directory or something else hope later i will update it soon



def server_update(path, key, value):
    value = str(value)  # Ensure the value is a string

    try:
        # Open the file for reading
        with open(path, "r") as file:
            lines = file.readlines()
        
        # Open the file for writing
        with open(path, "w") as file:
            for line in lines:
                if line.strip().startswith(key + "="):
                    file.write(f"{key}={value}\n")
                else:
                    file.write(line)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

filepath = "D:/pythonfordev/python-for-devops/day12/serverdetail.confi"
server_update(filepath, "MAX_CONNECTIONS", 1000)
