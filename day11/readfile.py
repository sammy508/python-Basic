import os
# Get the folder names from the user
folders = input("enter folder name, giving spaces: ").split()

#  it Gets the user's home directory
userprofile = os.path.expanduser('~') 


for folder in folders:
    folderpath = os.path.join(userprofile, folder)
  
    try:
     files = os.listdir(folderpath)
     print(f"Listed files for folder: {folderpath}")

     for file in files:
       print(f"{file}")

    except  FileNotFoundError:
     print(f"the folder {folderpath} you entered is not found")  # here f denotes the formatted string , 

    except PermissionError:
     print(f"Permission denied: {folderpath}")



# import os


# folders = input("Enter your folder names (separated by space): ").split()

# # Get the user's home directory
# userprofile = os.path.expanduser('~')

# # Iterate through each folder provided by the user
# for folder in folders:
#     folderpath = os.path.join(userprofile, folder)
#     try:
#         # List the files in the folder
#         files = os.listdir(folderpath)
#         print(f"Listed files for folder: {folderpath}")
        
#         # Print each file in the folder
#         for file in files:
#             print(f" - {file}")
#     except FileNotFoundError:
#         print(f"Folder not found: {folderpath}")
#     except PermissionError:
#         print(f"Permission denied: {folderpath}")
