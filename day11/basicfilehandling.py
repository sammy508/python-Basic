
# import os
# folders = input("input folder name by giving spaces : ").split() # here .split() changes it to list
# user = os.environ()
# for folder in folders:
#   files=  os.listdir(folder)
 
# print("`listed  for folder"+folder )

# for file in files:
#     os.listdir(file)
# print(file)      



# # Define the subfolders you want to check within the user's profile directory
# subfolders = input("Input subfolder names within the user directory, separated by spaces: ").split()

# # Get the current user's profile directory
# user_profile = os.environ['USERPROFILE']

# for subfolder in subfolders:
#     folder_path = os.path.join(user_profile, subfolder)
#     try:
#         files = os.listdir(folder_path)  # List the files in the subfolder
#         print(f"Listed files for folder: {folder_path}")
        
#         for file in files:
#             file_path = os.path.join(folder_path, file)  # Get the full path of the file
#             if os.path.isdir(file_path):  # Check if it's a directory
#                 sub_files = os.listdir(file_path)  # List the files in the sub-directory
#                 print(f"Contents of {file_path}: {sub_files}")
#             else:
#                 print(f"{file_path} is a file.")
#     except FileNotFoundError:
#         print(f"Folder not found: {folder_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")


import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()