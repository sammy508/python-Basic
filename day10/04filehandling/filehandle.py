try:
    # Attempt to open a file
    file = open('example.txt', 'r')
    
    # Try to read the content of the file
    content = file.read()
    print("File content:")
    print(content)
    
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'example.txt' was not found.")
    
except IOError:
    # Handle other I/O errors
    print("Error: An I/O error occurred.")
    
finally:
    print("sucessfully")